from notbank_python_sdk.core.converter import from_json_str
from notbank_python_sdk.core.either import Either
from notbank_python_sdk.error import ErrorCode,  NotbankException, StandardErrorResponse

from notbank_python_sdk.websocket.message_frame import MessageFrame
from notbank_python_sdk.websocket.message_type import MessageType


class PayloadGetter:
    @staticmethod
    def get(message_frame: MessageFrame) -> Either[NotbankException, str]:
        standard_error_response = from_json_str(
            StandardErrorResponse, message_frame.o)
        if standard_error_response.is_right() and standard_error_response.get().result == False:
            return Either.left(NotbankException.create(standard_error_response.get()))
        is_error_type = message_frame.m == MessageType.ERROR
        if is_error_type:
            return Either.left(NotbankException(ErrorCode.UNKNOWN, message_frame.o))
        return Either.right(message_frame.o)
