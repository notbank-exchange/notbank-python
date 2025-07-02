from typing import Callable,  Optional

from notbank_python_sdk.core.converter import from_json_str
from notbank_python_sdk.error import StandardErrorResponse
from notbank_python_sdk.websocket.callback_identifier import CallbackIdentifier
from notbank_python_sdk.websocket.message_frame import MessageFrame
from notbank_python_sdk.websocket.callback_manager import CallbackManager
from notbank_python_sdk.websocket.message_type import MessageType

MessageFrameCallback = Callable[[MessageFrame], None]


class WebsocketResponseHandler:
    _get_sequenced_callback: Callable[[int], Optional[MessageFrameCallback]]
    _get_subscription_callback: Callable[[
        str], Optional[Callable[[str], None]]]
    _on_failure: Callable[[Exception], None]

    def __init__(
        self,
        get_sequenced_callback: Callable[[int], Optional[MessageFrameCallback]],
        get_subscription_callback: Callable[[str], Optional[Callable[[str], None]]],
        on_failure: Callable[[Exception], None]
    ):
        self._get_sequenced_callback = get_sequenced_callback
        self._get_subscription_callback = get_subscription_callback
        self._on_failure = on_failure

    @staticmethod
    def create(callback_manager: CallbackManager, on_failure: Callable[[Exception], None]) -> 'WebsocketResponseHandler':
        return WebsocketResponseHandler(
            callback_manager.sequenced_callbacks.pop,
            callback_manager.subscription_callbacks.get,
            on_failure)

    def handle(self, message: str) -> None:
        try:
            message_frame = from_json_str(MessageFrame, message)
            if message_frame.is_left():
                self._on_failure(message_frame.get_left())
                return
            callback = self._get_sequenced_callback(message_frame.get().i)
            if callback:
                callback(message_frame.get())
                if self.is_error_message(message_frame.get()):
                    return
            callback_identifier = CallbackIdentifier.get_from_message_frame(
                message_frame.get())
            if callback_identifier is None:
                return
            subscription_callback = self._get_subscription_callback(
                callback_identifier)
            if subscription_callback is not None:
                subscription_callback(message_frame.get().o)
        except Exception as e:
            self._on_failure(e)

    def is_error_message(self, message_frame: MessageFrame) -> bool:
        is_error_type = message_frame.m == MessageType.ERROR
        if is_error_type:
            return True
        standard_error = from_json_str(StandardErrorResponse, message_frame.o)
        if standard_error.is_left():
            return False
        return standard_error.get().result is not None and not standard_error.get().result == False
