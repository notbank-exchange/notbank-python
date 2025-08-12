import threading
import time
from typing import Callable
from concurrent.futures import Executor, Future, ThreadPoolExecutor, TimeoutError
from notbank_python_sdk.error import NotbankException
from notbank_python_sdk.websocket.synched_var import SynchedValue
from notbank_python_sdk.websocket.websocket_connection import WebsocketConnection


class Pinger:
    _executor: Executor
    _stop_requested: SynchedValue[bool]
    _ping_interval_seconds: int
    _ping_timeout: int

    def __init__(
        self,
        executor: Executor,
        stop_requested: SynchedValue[bool],
        ping_interval_seconds: int,
        ping_timeout: int
    ) -> None:
        self._executor = executor
        self._stop_requested = stop_requested
        self._ping_interval_seconds = ping_interval_seconds
        self._ping_timeout = ping_timeout

    @staticmethod
    def create() -> 'Pinger':
        return Pinger(
            executor=ThreadPoolExecutor(1, "notbank pinger pool"),
            stop_requested=SynchedValue.create(False),
            ping_interval_seconds=5,
            ping_timeout=5
        )

    def _reset(self) -> None:
        self._stop_requested.set(False)

    def _should_stop(self) -> bool:
        return self._stop_requested.get()

    def _ping(self, ping_fn: Callable[[], None]) -> Future:
        return self._executor.submit(ping_fn)

    def _ping_forever(self, ping_fn: Callable[[], None], reconnect_fn: Callable[[], None]):
        while True:
            time.sleep(self._ping_interval_seconds)
            if self._should_stop():
                return
            try:
                future_pong = self._ping(ping_fn)
                future_pong.result(self._ping_timeout)
            except (TimeoutError, NotbankException) as e:
                if not self._should_stop():
                    reconnect_fn()
                return

    def restart(self, ping_fn: Callable[[], None], reconnect_fn: Callable[[], None]):
        self._stop_requested.set(False)
        threading.Thread(
            target=self._ping_forever,
            args=[ping_fn, reconnect_fn],
            name="notbank pinger",
            daemon=True
        ).start()

    def stop(self) -> None:
        self._stop_requested.set(True)
