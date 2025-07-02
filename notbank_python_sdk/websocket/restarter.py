

import logging
from threading import Thread
from time import sleep
from typing import Any, Callable, Dict, List, NamedTuple, Optional, TypeVar
from notbank_python_sdk.error import NotbankException
from notbank_python_sdk.models.authenticate_response import AuthenticateResponse
from notbank_python_sdk.requests_models.authenticate_request import AuthenticateRequest
from notbank_python_sdk.websocket.callback_manager import CallbackManager
from notbank_python_sdk.websocket.handler import WebsocketHandler
from notbank_python_sdk.websocket.subscription import Subscription, Unsubscription
from notbank_python_sdk.websocket.websocket_client_connection import WebsocketClientConnection
from notbank_python_sdk.websocket.websocket_manager import WebsocketManager
from notbank_python_sdk.websocket.websocket_requester import WebsocketRequester
from notbank_python_sdk.websocket.websocket_response_handler import WebsocketResponseHandler

T = TypeVar('T')


class ConnectionData(NamedTuple):
    uri: str
    on_open: Callable[[], None] = lambda: None
    on_reconnect: Callable[[], None] = lambda: None
    on_close: Callable[[Any, str], None] = lambda code, message: None
    on_failure: Callable[[Exception], None] = lambda e: None
    peek_message_in: Callable[[str], None] = lambda x: None
    peek_message_out: Callable[[str], None] = lambda x: None
    request_timeout: Optional[float] = None


class SubscriptionCache:
    _id: int
    _active_suscriptions: Dict[int, Subscription[Any]]

    def __init__(self):
        self._id = 0
        self._active_suscriptions = {}

    def save(self, subscription: Subscription[Any]) -> None:
        self._id += 1
        current_id = self._id
        self._active_suscriptions[current_id] = subscription

    def remove(self, unsubscription: Unsubscription[Any]) -> None:
        for callback_id in unsubscription.callback_ids:
            for sub_id in self._active_suscriptions:
                for active_callback in self._active_suscriptions[sub_id].callbacks:
                    if active_callback.id == callback_id:
                        del self._active_suscriptions[sub_id]
                        return

    def get_subscriptions(self) -> List[Subscription[Any]]:
        return list(self._active_suscriptions.values())


class WebsocketClientRestarter:
    _log: logging.Logger
    _websocket_client_connection: WebsocketClientConnection
    _callback_manager: CallbackManager
    _websocket_response_handler: WebsocketResponseHandler
    _connection_data: ConnectionData
    _subscription_cache: SubscriptionCache
    _authenticate_request: Optional[AuthenticateRequest]
    _requested_close: bool

    _reconnection_attempts: int
    _reconnecting: bool

    def __init__(
        self,
        websocket_client_connection: WebsocketClientConnection,
        callback_manager: CallbackManager,
        websocket_response_handler: WebsocketResponseHandler,
        connection_data: ConnectionData,
        subscription_cache: SubscriptionCache,
        authenticate_request: Optional[AuthenticateRequest],
        requested_close: bool,
        reconnection_attempts: int,
        reconnecting: bool,
    ):
        self._log = logging.getLogger(__name__)
        self._log.setLevel(logging.DEBUG)
        self._websocket_client_connection = websocket_client_connection
        self._callback_manager = callback_manager
        self._websocket_response_handler = websocket_response_handler
        self._connection_data = connection_data
        self._subscription_cache = subscription_cache
        self._authenticate_request = authenticate_request
        self._requested_close = requested_close
        self._reconnection_attempts = reconnection_attempts
        self._reconnecting = reconnecting

    @staticmethod
    def create(
        connection_data: ConnectionData,
        ping_interval: int
    ) -> 'WebsocketClientRestarter':
        callback_manager = CallbackManager.create()
        response_handler = WebsocketResponseHandler.create(
            callback_manager,
            connection_data.on_failure)
        restarter = WebsocketClientRestarter(
            None,  # type: ignore
            callback_manager,
            response_handler,
            connection_data,
            SubscriptionCache(),
            None,
            False,
            10,
            False
        )
        client = WebsocketClientRestarter._new_connection(
            callback_manager,
            response_handler,
            connection_data,
            connection_data.on_open,
            restarter._get_on_close(),
            restarter._get_on_failure()
        )
        restarter._websocket_client_connection = client
        return restarter

    def get_connection(self) -> WebsocketClientConnection:
        return self._websocket_client_connection

    def subscribe(self, subscription: Subscription[T]) -> T:
        result = self.get_connection().subscribe(subscription)
        self._subscription_cache.save(subscription)
        return result

    def unsubscribe(self, unsubscription: Unsubscription[T]) -> T:
        self._subscription_cache.remove(unsubscription)
        result = self.get_connection().unsubscribe(unsubscription)
        return result

    def close(self) -> None:
        self._requested_close = True
        self.get_connection().close()

    def authenticate_user(self, authenticate_request: AuthenticateRequest) -> AuthenticateResponse:
        return self.get_connection().authenticate_user(authenticate_request)

    def _reconnect(self) -> None:
        self._log.debug("reconnecting websocket connection")
        self._reconnecting = True
        self._close_old_connection()
        new_connection = self.restablish_connection()
        if self._authenticate_request:
            new_connection.authenticate_user(self._authenticate_request)
        for subscription in self._subscription_cache.get_subscriptions():
            new_connection.subscribe(subscription)
            sleep(1)
        self._websocket_client_connection = new_connection
        self._log.debug("websocket connection reconnected")

    def restablish_connection(self):
        while True:
            try:
                new_connection = self._new_connection(
                    self._callback_manager,
                    self._websocket_response_handler,
                    self._connection_data,
                    self._get_on_reconnect(),
                    self._get_on_close(),
                    self._get_on_failure())
                new_connection.connect()
                return new_connection
            except NotbankException:
                self._log.debug("connection failed, trying again in 10 sec")
                sleep(10)

    def _close_old_connection(self):
        try:
            self.get_connection().close()
        except:
            self._log.debug("unable to close old connection")

    def _get_on_reconnect(self) -> Callable[[], None]:
        def on_reconnect() -> None:
            self._reconnecting = False
            self._connection_data.on_reconnect()
        return on_reconnect

    def _get_on_close(self) -> Callable[[Any, str], None]:
        def reconnect_on_unexpected_close(code: Any, message: str) -> None:
            if self._requested_close:
                self._connection_data.on_close(code, message)
                return
        return reconnect_on_unexpected_close

    def _get_on_failure(self) -> Callable[[Exception], None]:
        def reconnect_on_unexpected_failure(err: Exception) -> None:
            if not self._reconnecting:
                self._reconnect()
        return reconnect_on_unexpected_failure

    @staticmethod
    def _new_connection(
        callback_manager: CallbackManager,
        websocket_response_handler: WebsocketResponseHandler,
        connection_data: ConnectionData,
        on_open: Callable[[], None],
        on_close: Callable[[Any, str], None],
        on_failure: Callable[[Exception], None],
    ) -> 'WebsocketClientConnection':

        websocket_manager = WebsocketManager(
            WebsocketHandler(
                websocket_response_handler.handle,
                on_open=on_open,
                on_close=on_close,
                on_failure=on_failure),
            connection_data.uri,
            connection_data.peek_message_in,
            connection_data.peek_message_out)
        websocket_requester = WebsocketRequester.create(
            callback_manager,
            websocket_manager.send,
            connection_data.on_failure,
            request_timeout=connection_data.request_timeout,
        )
        websocket_response_handler = WebsocketResponseHandler.create(
            callback_manager,
            connection_data.on_failure)
        return WebsocketClientConnection(
            callback_manager,
            websocket_manager,
            websocket_requester,
            websocket_response_handler)
