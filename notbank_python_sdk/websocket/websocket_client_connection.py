import simplejson as json
from typing import Any, Callable, Optional
from notbank_python_sdk.core.endpoints import Endpoints
from notbank_python_sdk.models.authenticate_response import AuthenticateResponse
from notbank_python_sdk.models.pong import Pong
from notbank_python_sdk.parsing import parse_response_fn
from notbank_python_sdk.requests_models.authenticate_request import AuthenticateRequest

from notbank_python_sdk.core.authenticator import Authenticator
from notbank_python_sdk.client_connection import T
from notbank_python_sdk.core.converter import from_dict, to_dict
from notbank_python_sdk.core.endpoint_category import EndpointCategory
from notbank_python_sdk.error import NotbankException, ErrorCode
from notbank_python_sdk.core.response_handler import ResponseHandler
from notbank_python_sdk.websocket.callback_manager import CallbackManager
from notbank_python_sdk.websocket.handler import WebsocketHandler
from notbank_python_sdk.websocket.subscription import Subscription, Unsubscription
from notbank_python_sdk.websocket.websocket_manager import WebsocketManager
from notbank_python_sdk.websocket.websocket_requester import WebsocketRequester
from notbank_python_sdk.websocket.websocket_response_handler import WebsocketResponseHandler


class WebsocketClientConnection:
    _callback_manager: CallbackManager
    _websocket_manager: WebsocketManager
    _websocket_requester: WebsocketRequester
    _websocket_response_hanlder: WebsocketResponseHandler

    def __init__(
            self,
            callback_manager: CallbackManager,
            websocket_manager: WebsocketManager,
            websocket_requester: WebsocketRequester,
            websocket_response_handler: WebsocketResponseHandler):
        self._callback_manager = callback_manager
        self._websocket_manager = websocket_manager
        self._websocket_requester = websocket_requester
        self._websocket_response_hanlder = websocket_response_handler

    @staticmethod
    def create(uri: str,
               on_open: Callable[[], None] = lambda: None,
               on_close: Callable[[Any, str], None] = lambda code, message: None,
               on_failure: Callable[[Exception], None] = lambda e: None,
               peek_message_in: Callable[[str], None] = lambda x: None,
               peek_message_out: Callable[[str], None] = lambda x: None,
               request_timeout: Optional[float] = None,
               ) -> 'WebsocketClientConnection':
        callback_manager = CallbackManager.create()
        response_handler = WebsocketResponseHandler.create(
            callback_manager,
            on_failure)
        websocket_manager = WebsocketManager(
            WebsocketHandler(
                response_handler.handle,
                on_open,
                on_close,
                on_failure),
            uri,
            peek_message_in,
            peek_message_out)
        websocket_requester = WebsocketRequester.create(
            callback_manager,
            websocket_manager.send,
            on_failure,
            request_timeout=request_timeout,
        )
        websocket_response_handler = WebsocketResponseHandler.create(
            callback_manager,
            on_failure)
        return WebsocketClientConnection(
            callback_manager,
            websocket_manager,
            websocket_requester,
            websocket_response_handler)

    def connect(self) -> None:
        self._websocket_manager.connect()

    def close(self) -> None:
        self._websocket_manager.close()

    def subscribe(self, subscription: Subscription[T]) -> T:
        subscription_result_getter = self._websocket_requester.subscribe(
            subscription)
        result = subscription_result_getter()
        return self.handle_result(subscription.parse_response_fn, result)

    def unsubscribe(self, unsubscription: Unsubscription[T]) -> T:
        unsubscription_result_getter = self._websocket_requester.unsubscribe(
            unsubscription)
        result = unsubscription_result_getter()
        return self.handle_result(unsubscription.parse_response_fn, result)

    def request(
            self,
            endpoint: str,
            endpoint_category: EndpointCategory,
            request_message: Any,
            parse_response_fn: Callable[[Any], T]) -> T:
        if endpoint_category != EndpointCategory.AP:
            raise NotbankException(
                ErrorCode.INVALID_REQUEST, "websocket server only supports ap endpoints")
        result_getter = self._websocket_requester.request(
            endpoint, request_message)
        result = result_getter()
        return self.handle_result(parse_response_fn, result)

    def authenticate_user(self, authenticate_request: AuthenticateRequest) -> AuthenticateResponse:
        request_data = Authenticator.convert_data(authenticate_request)
        return self.request(Endpoints.AUTHENTICATE_USER, EndpointCategory.AP, to_dict(request_data), lambda data: from_dict(AuthenticateResponse, data))

    def ping(self) -> None:
        result = self.request(
            Endpoints.PING, EndpointCategory.AP, None, parse_response_fn(Pong, ["msg"]))
        return

    def handle_result(self, parse_response_fn: Callable[[Any], T], result: Any) -> T:
        if result.is_left():
            raise result.get_left()
        data_dict = json.loads(result.get(), use_decimal=True)
        return ResponseHandler.handle_response_data(EndpointCategory.AP, parse_response_fn, data_dict)
