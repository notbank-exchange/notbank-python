from enum import Enum
from typing import Any, Callable, TypeVar

from notbank_python_sdk.error import ErrorCode, NotbankException, StandardErrorResponse
from dacite.data import Data
from dacite import Config, MissingValueError, from_dict as dacite_from_dict

T = TypeVar('T')


class ApDataHandler:
    @staticmethod
    def handle_ap_data(parse_response: Callable[[Data], T], response_data: Any) -> T:
        try:
            standard_response = dacite_from_dict(
                StandardErrorResponse,
                response_data,
                config=Config(cast=[Enum]))
            if standard_response.result is False:
                raise NotbankException.create(standard_response)
        except MissingValueError:
            pass
        try:
            return parse_response(response_data)
        except MissingValueError as e:
            raise NotbankException(
                ErrorCode.CONFIGURATION_ERROR,
                f"notbank sdk badly configured. {e}")
