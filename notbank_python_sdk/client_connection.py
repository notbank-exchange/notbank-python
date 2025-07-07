from enum import Enum
from typing import Any, Callable, Dict, List, TypeVar

from notbank_python_sdk.error import ErrorCode, NotbankException
from notbank_python_sdk.requests_models.authenticate_request import AuthenticateRequest
from notbank_python_sdk.models.authenticate_response import AuthenticateResponse
from notbank_python_sdk.websocket.subscription import Subscription, Unsubscription
from notbank_python_sdk.core.endpoint_category import EndpointCategory


T = TypeVar('T')

ParseResponseFn = Callable[[Any], T]
ParseResponseListFn = Callable[[Any], List[T]]
RequestMethodFn = Callable[[str, EndpointCategory, Any, ParseResponseFn[T]], T]
AuthenticateMethodFn = Callable[[AuthenticateRequest], AuthenticateResponse]
SubscribeFn = Callable[[Subscription[T]], T]
UnsubscribeFn = Callable[[Unsubscription[T]], T]


class RequestType(Enum):
    POST = 0
    GET = 1
    DELETE = 2


class ClientConnection:
    def __init__(
        self,
        post_request: RequestMethodFn,
        get_request: RequestMethodFn,
        delete_request: RequestMethodFn,
        subscribe: SubscribeFn,
        unsubscribe: UnsubscribeFn,
        authenticate_user: AuthenticateMethodFn,
        connect: Callable[[], None],
        close: Callable[[], None]
    ):
        self._request_methods: Dict[RequestType, RequestMethodFn] = {
            RequestType.POST: post_request,
            RequestType.GET: get_request,
            RequestType.DELETE: delete_request,
        }
        self._subscribe = subscribe
        self._unsubscribe = unsubscribe
        self._authenticate_user = authenticate_user
        self._connect = connect
        self._close = close

    def request(
        self,
        endpoint: str,
        endpoint_category: EndpointCategory,
        request_data: Any,
        parse_response_fn: ParseResponseFn[T],
        request_type: RequestType = RequestType.POST,
    ) -> T:
        request_method = self._request_methods.get(request_type)
        if request_method is None:
            raise NotbankException(
                ErrorCode.CONFIGURATION_ERROR, f"no request method found for type: {request_type}")
        return request_method(endpoint, endpoint_category, request_data, parse_response_fn)

    def subscribe(self, subscription: Subscription[T]) -> T:
        return self._subscribe(subscription)

    def unsubscribe(self, unsubscription: Unsubscription[T]) -> T:
        return self._unsubscribe(unsubscription)

    def connect(self) -> None:
        self._connect()

    def close(self) -> None:
        self._close()

    def authenticate(self, authenticate_request: AuthenticateRequest) -> AuthenticateResponse:
        return self._authenticate_user(authenticate_request)
