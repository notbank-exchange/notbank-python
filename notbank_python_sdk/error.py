from dataclasses import dataclass
from enum import Enum
from typing import Optional


class ErrorCode(Enum):
    TIMED_OUT = -300
    CONFIGURATION_ERROR = -200
    INVALID_RESPONSE = -100
    UNKNOWN = -1
    SUCCESS = 0
    NOT_AUTHORIZED = 20
    INVALID_REQUEST = 100
    OPERATION_FAILED = 101
    SERVER_ERROR = 102
    RESOURCE_NOT_FOUND = 104


@dataclass
class StandardErrorResponse:
    result: bool
    errormsg: Optional[str] = None
    errorcode: ErrorCode = ErrorCode.SUCCESS
    detail: Optional[str] = None


def _get_message(standard_error_response: StandardErrorResponse) -> str:
    message = standard_error_response.errormsg or ""
    detail = standard_error_response.detail or ""
    return message + ". " + detail


class NotbankException(Exception):
    def __init__(self, code: ErrorCode, message: str):
        self.code = code
        super().__init__(message)

    @staticmethod
    def create(standard_error_response: StandardErrorResponse) -> 'NotbankException':
        message = _get_message(standard_error_response)
        return NotbankException(standard_error_response.errorcode, message)
