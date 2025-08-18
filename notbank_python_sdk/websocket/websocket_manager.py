from dataclasses import dataclass
from queue import Empty, Queue
from threading import Thread
from typing import Any, Callable, Optional
from notbank_python_sdk.websocket.synched_var import SynchedValue

import websocket

from notbank_python_sdk.error import ErrorCode, NotbankException, NotbankException


@dataclass
class Hooks:
    on_message: Callable[[Any, str], None]
    on_open: Callable[[Any], None]
    on_close: Callable[[Any, int, str], None]
    on_error: Callable[[Any, Exception], None]


class WebsocketManager:
    _uri: str
    _connected_signal: Queue
    _peek_message_out: Callable[[str], None]
    _connected: SynchedValue[bool]
    _hooks: Hooks
    _ws: websocket.WebSocketApp
    _thread: Optional[Thread]

    def __init__(self,
                 handler,
                 host,
                 peek_message_in: Callable[[str], None] = lambda x: None,
                 peek_message_out: Callable[[str], None] = lambda x: None):
        self._uri = self._build_url(host)
        self._connected = SynchedValue.create(False)
        self._connected_signal = Queue(1)
        self._peek_message_out = peek_message_out
        self._thread = None

        def on_message(ws, message):
            peek_message_in(message)
            handler.handle(message)

        def on_error(ws, error):
            handler.on_error(error)

        def on_close(ws, code: int, message: str):
            handler.on_close(code, message)

        def on_open(ws):
            self._connected.set(True)
            self._connected_signal.put(True)
            handler.on_open()
        self._hooks = Hooks(
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error
        )

    def connect(self, timeout: float = 5):
        self._connected.set(False)
        self._ws = websocket.WebSocketApp(
            self._uri,
            on_message=self._hooks.on_message,
            on_error=self._hooks.on_error,
            on_close=self._hooks.on_close,
            on_open=self._hooks.on_open,
        )
        self._thread = Thread(
            target=self._ws.run_forever,
            name="notbank websocket",
            daemon=True)
        self._thread.start()
        try:
            self._connected_signal.get(block=True, timeout=timeout)
            return
        except Empty:
            self.close()
            raise NotbankException(
                ErrorCode.TIMED_OUT, "unable to connect to server. connection timed out")

    def send(self, msg: str) -> None:
        if not self._connected.get() or self._thread is None or not self._thread.is_alive():
            raise NotbankException(
                ErrorCode.OPERATION_FAILED, "websocket not connected")
        self._peek_message_out(msg)
        self._ws.send(msg)

    def close(self):
        try:
            self._ws.close()
            self._connected.set(False)
        except Exception as e:
            self._hooks.on_error(self._ws, e)
        if self._thread is None:
            return
        self._thread.join(5)

    def _build_url(self, host: str) -> str:
        return "wss://" + host + "/wsgateway/"
