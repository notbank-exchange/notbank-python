import threading
import time
from typing import Callable
from concurrent.futures import Executor, Future, ThreadPoolExecutor
from notbank_python_sdk.error import NotbankException
from notbank_python_sdk.websocket.synched_var import SynchedValue
from notbank_python_sdk.websocket.websocket_connection import WebsocketConnection


class Pinger:
    _executor: Executor
    _stop_requested: SynchedValue[bool]

    def __init__(self, executor: Executor, stop_requested: SynchedValue[bool]) -> None:
        self._executor = executor
        self._stop_requested = stop_requested

    @staticmethod
    def create() -> 'Pinger':
        executor = ThreadPoolExecutor(1, "notbank ping")
        stop_requested = SynchedValue.create(False)
        return Pinger(executor, stop_requested)

    def _reset(self) -> None:
        self._stop_requested.set(False)

    def _should_stop(self) -> bool:
        return self._stop_requested.get()

    def _ping(self, connection: WebsocketConnection) -> Future:
        return self._executor.submit(connection.ping)

    def _ping_forever(self, connection: WebsocketConnection, reconnect: Callable[[], None]):
        while True:
            if self._should_stop():
                return
            try:
                time.sleep(10)
                future_pong = self._ping(connection)
                future_pong.result(10)
                continue
            except (TimeoutError, NotbankException):
                if not self._should_stop():
                    reconnect()
                return

    def restart(self, connection: WebsocketConnection, restart: Callable[[], None]):
        threading.Thread(
            target=self._ping_forever,
            args=[connection, restart],
            daemon=True
        ).start()

    def stop(self) -> None:
        self._stop_requested.set(True)
