from typing import Any, Callable, TypeVar
from notbank_python_sdk.core.endpoint_category import EndpointCategory
from notbank_python_sdk.models.authenticate_response import AuthenticateResponse
from notbank_python_sdk.requests_models.authenticate_request import AuthenticateRequest
from notbank_python_sdk.websocket.subscription import Subscription, Unsubscription
from notbank_python_sdk.websocket.websocket_restarter.restarter import Restarter

T = TypeVar("T")


class RestartingWebsocketConnection:
    _restarter: Restarter

    def __init__(self, restarter: Restarter):
        self._restarter = restarter

    def connect(self) -> None:
        self._restarter.reconnect()

    def close(self) -> None:
        self._restarter.close()

    def subscribe(self, subscription: Subscription[T]) -> T:
        subscription_result = self._restarter.get_connection().subscribe(subscription)
        self._restarter.get_resubscriber().save(subscription)
        return subscription_result

    def unsubscribe(self, unsubscription: Unsubscription[T]) -> T:
        unsubscription_result = self._restarter.get_connection().unsubscribe(unsubscription)
        self._restarter.get_resubscriber().remove(unsubscription)
        return unsubscription_result

    def request(
            self,
            endpoint: str,
            endpoint_category: EndpointCategory,
            request_message: Any,
            parse_response_fn: Callable[[Any], T]) -> T:
        return self._restarter.get_connection().request(endpoint, endpoint_category, request_message, parse_response_fn)

    def authenticate_user(self, authenticate_request: AuthenticateRequest) -> AuthenticateResponse:
        authentication_response = self._restarter.get_connection(
        ).authenticate_user(authenticate_request)
        if authentication_response.authenticated:
            self._restarter.get_reauther().update_authenticate_fn(
                lambda connection: connection.authenticate_user(authenticate_request))
        return authentication_response
