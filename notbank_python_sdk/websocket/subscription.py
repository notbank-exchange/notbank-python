from typing import Any, Callable, Generic, List, TypeVar

from notbank_python_sdk.websocket.subscription_handler import Callback

T = TypeVar('T')


class Subscription(Generic[T]):
    endpoint: str
    message: Any
    callbacks: List[Callback]
    parse_response_fn: Callable[[Any], T]

    def __init__(
        self,
        endpoint: str,
        message: Any,
        callbacks: List[Callback],
        parse_response_fn: Callable[[Any], T],
    ):
        self.endpoint = endpoint
        self.message = message
        self.callbacks = callbacks
        self.parse_response_fn = parse_response_fn


class Unsubscription(Generic[T]):
    endpoint: str
    message: Any
    callback_ids: List[str]
    parse_response_fn: Callable[[Any], T]

    def __init__(
        self,
        endpoint: str,
        message: Any,
        callback_ids: List[str],
        parse_response_fn: Callable[[Any], T],
    ):
        self.endpoint = endpoint
        self.message = message
        self.callback_ids = callback_ids
        self.parse_response_fn = parse_response_fn
