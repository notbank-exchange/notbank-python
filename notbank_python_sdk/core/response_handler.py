from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Generic, Optional, TypeVar

import requests

from notbank_python_sdk.core.endpoint_category import EndpointCategory
from notbank_python_sdk.error import ErrorCode, NotbankException, StandardErrorResponse
from dacite.data import Data
from dacite import Config, MissingValueError, from_dict as dacite_from_dict
T = TypeVar('T')


class NBResponseStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"


@dataclass
class NBResponse(Generic[T]):
    status: NBResponseStatus
    message: Optional[str] = None
    data: Optional[Any] = None
    total: Optional[int] = None


class ResponseHandler:
    @staticmethod
    def handle_response_data(endpoint_category: EndpointCategory, parse_response: Callable[[Any], T], response: requests.Response) -> T:
        if endpoint_category == EndpointCategory.AP:
            return ResponseHandler.handle_ap_response_data(parse_response, response)
        if endpoint_category == EndpointCategory.NB or endpoint_category == EndpointCategory.NB_PAGE:
            return ResponseHandler.handle_nb_response_data(response, parse_response, endpoint_category)
        raise NotbankException(ErrorCode.CONFIGURATION_ERROR,
                               f"unable to handle server response. handler for endpoint category {endpoint_category} not set")

    @staticmethod
    def handle_nb_response_data(response: requests.Response, parse_response: Callable[[Any], T], endpoint_category: EndpointCategory) -> T:
        response_data = ResponseHandler.get_response_data(response)
        try:
            nb_response = dacite_from_dict(
                NBResponse,
                response_data,
                config=Config(cast=[Enum]))
            if nb_response.status is NBResponseStatus.ERROR:
                error_message = nb_response.message if nb_response.message else ""
                raise NotbankException(
                    ErrorCode.SERVER_ERROR, f"(http code={response.status_code}) {error_message}")
            data = response_data
            if endpoint_category == EndpointCategory.NB:
                data = nb_response.data
            return parse_response(data)
        except MissingValueError as e:
            raise NotbankException(
                ErrorCode.CONFIGURATION_ERROR,
                f"notbank sdk badly configured. {e}")

    @staticmethod
    def handle_ap_response_data(parse_response: Callable[[Data], T], response: requests.Response) -> T:
        if response.status_code < 200 or 400 <= response.status_code:
            raise NotbankException(
                ErrorCode.SERVER_ERROR,
                f"http error. (code={response.status_code}) {response.text}")
        response_data = ResponseHandler.get_response_data(response)
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

    @staticmethod
    def get_response_data(response):
        try:
            return response.json()
        except requests.JSONDecodeError as e:
            raise NotbankException(
                ErrorCode.INVALID_RESPONSE,
                f"unable to decode json response: {response.text}. {e}")
