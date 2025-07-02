import logging
from queue import Empty, Queue
from threading import Thread
from typing import Callable

import websocket

from notbank_python_sdk.error import ErrorCode, NotbankException, NotbankException


class WebsocketManager:
    def __init__(self,
                 handler,
                 host,
                 peek_message_in: Callable[[str], None] = lambda x: None,
                 peek_message_out: Callable[[str], None] = lambda x: None):

        self._log = logging.getLogger(__name__)
        self._log.setLevel(logging.DEBUG)
        self.uri = self._build_url(host)
        self.connected = False
        self._connected_signal = Queue(1)
        self._peek_message_in = peek_message_in
        self._peek_message_out = peek_message_out

        def on_message(ws, message):
            self._peek_message_in(message)
            handler.handle(message)

        def on_error(ws, error):
            self._log.error("websocket error: " + str(error))
            handler.on_error(error)

        def on_close(ws, code: int, message: str):
            self._log.debug('websocket connection closed')
            handler.on_close(code, message)

        def on_open(ws):
            self.connected = True
            self._connected_signal.put(True)
            handler.on_open()

        self.ws = websocket.WebSocketApp(
            self.uri,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
            on_open=on_open,
        )

        self.thread = Thread(target=self.ws.run_forever)

    def connect(self):
        self.thread.start()
        try:
            self._connected_signal.get(block=True, timeout=5)
            return
        except Empty:
            raise NotbankException(ErrorCode.CONFIGURATION_ERROR, "")

    def send(self, msg: str) -> None:
        if not self.thread.is_alive():
            raise ConnectionError('websocket connection is not active')
        self._peek_message_out(msg)
        self.ws.send(msg)

    def close(self):
        try:
            self.ws.close()
        except Exception as e:
            self._log.error("unable to close socket: " + str(e))
        self.connected = False
        self.thread.join(5)

    def _build_url(self, host: str) -> str:
        return "wss://" + host + "/wsgateway/"
