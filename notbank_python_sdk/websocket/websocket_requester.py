from queue import Empty, Full, Queue
from typing import Any, Callable, List, Optional, TypeVar

import simplejson as json
from queue import Queue
from typing import Callable, List, TypeVar
from notbank_python_sdk.core.converter import to_json_str
from notbank_python_sdk.core.either import Either
from notbank_python_sdk.error import ErrorCode, NotbankException
from notbank_python_sdk.websocket.callback_manager import CallbackManager

from notbank_python_sdk.websocket.message_frame import MessageFrame
from notbank_python_sdk.websocket.message_type import MessageType
from notbank_python_sdk.websocket.payload_getter import PayloadGetter
from notbank_python_sdk.websocket.subscription import Subscription, Unsubscription
from notbank_python_sdk.websocket.subscription_handler import Callback

T = TypeVar('T')
MessageFrameCallback = Callable[[MessageFrame], None]


class WebsocketRequester:
    _store_subscription_callback: Callable[[str, Callable[[str], None]], None]
    _remove_subscription_callback: Callable[[str], None]
    _store_callback: Callable[[MessageFrameCallback], int]
    _web_socket_send_fn: Callable[[str], None]
    _on_failure: Callable[[Exception], None]
    _request_timeout: Optional[float]

    def __init__(
        self,
        store_subscription_callback: Callable[[str, Callable[[str], None]], None],
        remove_subscription_callback: Callable[[str], None],
        store_callback: Callable[[MessageFrameCallback], int],
        web_socket_send_fn: Callable[[str], None],
        on_failure: Callable[[Exception], None],
        request_timeout: Optional[float] = None
    ):
        self._store_subscription_callback = store_subscription_callback
        self._remove_subscription_callback = remove_subscription_callback
        self._store_callback = store_callback
        self._web_socket_send_fn = web_socket_send_fn
        self._on_failure = on_failure
        self._request_timeout = request_timeout

    @staticmethod
    def create(
            callback_manager: CallbackManager,
            web_socket_send_fn: Callable[[str], None],
            on_failure: Callable[[Exception], None],
            request_timeout: Optional[float] = None,
    ) -> 'WebsocketRequester':
        return WebsocketRequester(
            store_subscription_callback=callback_manager.subscription_callbacks.add,
            remove_subscription_callback=callback_manager.subscription_callbacks.remove,
            store_callback=callback_manager.sequenced_callbacks.put,
            web_socket_send_fn=web_socket_send_fn,
            on_failure=on_failure,
            request_timeout=request_timeout,
        )

    def subscribe(self, subscription: Subscription[Any]) -> Callable[[], Either[NotbankException, str]]:
        for callback in subscription.callbacks:
            self._store_subscription_callback(
                callback.id, callback.builder(self._on_failure))
        return self._request_to_queue(subscription.endpoint, subscription.message, MessageType.REQUEST)

    def unsubscribe(self, unsubscription: Unsubscription):
        for callback_id in unsubscription.callback_ids:
            self._remove_subscription_callback(callback_id)
        return self._request_to_queue(unsubscription.endpoint, unsubscription.message, MessageType.REQUEST)

    def request(self, endpoint: str, message: str) -> Callable[[], Either[NotbankException, str]]:
        return self._request_to_queue(endpoint, message, MessageType.REQUEST)

    def _request_to_queue(self, endpoint: str, message: str, message_type: MessageType) -> Callable[[], Either[NotbankException, str]]:
        response_buffer = Queue(maxsize=1)
        sequence_number = self._store_callback(
            self._handle_request_response(response_buffer))
        message_frame = MessageFrame(
            message_type, sequence_number, endpoint, json.dumps(message, use_decimal=True))
        message_frame_str = to_json_str(
            message_frame, {MessageType: lambda message_type: message_type.value})
        self._web_socket_send_fn(message_frame_str)

        def wait_response() -> Either[NotbankException, str]:
            try:
                return response_buffer.get(timeout=self._request_timeout)
            except Empty:
                return Either.left(NotbankException(ErrorCode.TIMED_OUT, "request timed out"))
        return wait_response

    def _handle_request_response(self, response_buffer: Queue):
        def response_handler(message_frame: MessageFrame):
            data = PayloadGetter.get(message_frame)
            try:
                response_buffer.put(data, block=False)
            except Full:
                pass
        return response_handler
