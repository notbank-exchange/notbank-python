

from concurrent.futures import Executor, ThreadPoolExecutor, TimeoutError

from typing import Any, Optional, TypeVar
from notbank_python_sdk.error import ErrorCode, NotbankException
from notbank_python_sdk.websocket.callback_manager import CallbackManager
from notbank_python_sdk.websocket.connection_configuration import ConnectionConfiguration
from notbank_python_sdk.websocket.handler import WebsocketHandler
from notbank_python_sdk.websocket.websocket_restarter.pinger import Pinger
from notbank_python_sdk.websocket.websocket_restarter.reauther import Reauther
from notbank_python_sdk.websocket.websocket_restarter.resubscriber import Resubscriber
from notbank_python_sdk.websocket.synched_var import SynchedValue
from notbank_python_sdk.websocket.websocket_connection import WebsocketConnection
from notbank_python_sdk.websocket.websocket_manager import WebsocketManager
from notbank_python_sdk.websocket.websocket_requester import WebsocketRequester
from notbank_python_sdk.websocket.websocket_response_handler import WebsocketResponseHandler

T = TypeVar('T')

class Restarter:
    _executor: Executor
    _connection: Optional[WebsocketConnection]
    _connection_configuration: ConnectionConfiguration
    _pinger: Pinger
    _resubscriber: Resubscriber
    _reauther: Reauther
    _close_requested: SynchedValue[bool]
    _reconnecting: SynchedValue[bool]

    def __init__(
        self,
        executor: Executor,
        connection: Optional[WebsocketConnection],
        connection_configuration: ConnectionConfiguration,
        pinger: Pinger,
        resubscriber: Resubscriber,
        reauther: Reauther,
        requested_close: SynchedValue[bool],
        reconnecting: SynchedValue[bool],
    ):
        self._executor = executor
        self._connection = connection
        self._connection_configuration = connection_configuration
        self._pinger = pinger
        self._resubscriber = resubscriber
        self._reauther = reauther
        self._close_requested = requested_close
        self._reconnecting = reconnecting

    @staticmethod
    def create(connection_configuration: ConnectionConfiguration) -> 'Restarter':
        executor = ThreadPoolExecutor(1, "notbank restarter pool")
        return Restarter(
            executor,
            connection=None,
            connection_configuration=connection_configuration,
            pinger=Pinger(executor, SynchedValue.create(False), 10, 5),
            resubscriber=Resubscriber(),
            reauther=Reauther(),
            requested_close=SynchedValue.create(False),
            reconnecting=SynchedValue.create(False)
        )

    def get_resubscriber(self) -> Resubscriber:
        return self._resubscriber

    def get_reauther(self) -> Reauther:
        return self._reauther

    def get_connection(self) -> WebsocketConnection:
        if self._connection is None:
            raise NotbankException(
                ErrorCode.OPERATION_FAILED, "websocket not started")
        if self._reconnecting.get():
            raise NotbankException(
                ErrorCode.OPERATION_FAILED, "websocket reconnecting")
        return self._connection

    def _on_close(self, code: Any, message: str) -> None:
        if self._reconnecting or not self._close_requested.get():
            return
        self._connection_configuration.on_close(code, message)

    def _on_failure(self, exception: Exception) -> None:
        if self._reconnecting:
            return
        self._connection_configuration.on_failure(exception)

    def _new_connection(self) -> WebsocketConnection:
        callback_manager = CallbackManager.create()
        websocket_response_handler = WebsocketResponseHandler.create(
            callback_manager,
            self._connection_configuration.on_failure)
        websocket_handler = WebsocketHandler(
            websocket_response_handler.handle,
            on_open=self._connection_configuration.on_open,
            on_close=self._on_close,
            on_failure=self._on_failure)
        websocket_manager = WebsocketManager(
            websocket_handler,
            self._connection_configuration.uri,
            self._connection_configuration.peek_message_in,
            self._connection_configuration.peek_message_out)
        websocket_requester = WebsocketRequester.create(
            callback_manager,
            websocket_manager.send,
            self._on_failure,
            request_timeout=self._connection_configuration.request_timeout,
        )
        websocket_response_handler = WebsocketResponseHandler.create(
            callback_manager,
            self._on_failure)
        return WebsocketConnection(
            callback_manager,
            websocket_manager,
            websocket_requester,
            websocket_response_handler)

    def _close_current_connection(self) -> None:
        self._pinger.stop()
        if self._connection is not None:
            self._connection.close()

    def _connect(self) -> None:
        if self._connection is None:
            raise NotbankException(
                ErrorCode.OPERATION_FAILED, "websocket not started")
        while not self._close_requested.get():
            connected_future = self._executor.submit(self._connection.connect)
            try:
                connected_future.result(10)
                return
            except (TimeoutError, NotbankException):
                # try again
                pass

    def close(self) -> None:
        self._close_requested.set(True)
        self._close_current_connection()

    def reconnect(self) -> None:
        if self._reconnecting.get() or self._close_requested.get():
            return
        self._reconnecting.set(True)
        self._close_current_connection()
        self._connection = self._new_connection()
        self._connect()
        self._reauther.reauthenticate(self._connection)
        self._resubscriber.resubscribe(self._connection)
        self._pinger.restart(self._connection.ping, self.reconnect)
        self._reconnecting.set(False)
