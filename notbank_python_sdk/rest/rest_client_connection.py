from typing import Any, Callable, List, Optional, TypeVar

import requests
from dacite.data import Data

from notbank_python_sdk.error import ErrorCode, NotbankException
from notbank_python_sdk.models.authenticate_response import AuthenticateResponse
from notbank_python_sdk.requests_models.authenticate_request import AuthenticateRequest
from notbank_python_sdk.core.authenticator import Authenticator
from notbank_python_sdk.core.converter import from_dict, to_dict
from notbank_python_sdk.core.response_handler import ResponseHandler
from notbank_python_sdk.core.endpoint_category import EndpointCategory

T = TypeVar('T')
ParseResponseFn = Callable[[Any], T]

AUTHENTICATE_USER_ENDPOINT = "AuthenticateUser"
AUTHENTICATE_2FA = "Authenticate2FA"


class RestClientConnection:
    NAME = "Notbank"
    VERSION = "0.0.1"
    _host: str
    _rest_session: requests.Session
    _peek_message_in: Callable[[str], None]
    _peek_message_out: Callable[[str, Any, Any, str, dict], None]

    def __init__(
            self,
            host: str,
            ap_token: Optional[str] = None,
            peek_message_in: Callable[[str], None] = lambda a: None,
            peek_message_out: Callable[[str, Any, Any, str, dict], None] = lambda a, b, c, d, e: None,
    ):
        self._host = self._get_host_url(host)
        self._rest_session = requests.Session()
        self._rest_session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': f'{self.NAME} Python SDK v{self.VERSION}',
        })
        self._update_headers(ap_token)
        self._peek_message_in = peek_message_in
        self._peek_message_out = peek_message_out

    def _get_host_url(self, host: str) -> str:
        return "https://" + host

    def _update_headers(self, ap_token: Optional[str], header_to_remove_list: List[str] = []) -> None:
        for header_to_remove in header_to_remove_list:
            del self._rest_session.headers[header_to_remove]
        if ap_token is not None:
            self._rest_session.headers.update({
                'aptoken': ap_token,
            })

    def close(self) -> None:
        self._rest_session.close()

    def _get_endpoint_url(self, endpoint: str, endpoint_category: EndpointCategory,) -> str:
        url = self._host + "/" + endpoint_category.val + "/" + endpoint
        return url

    def get(self, endpoint: str, endpoint_category: EndpointCategory, params: Any, parse_response: ParseResponseFn[T]) -> T:
        url = self._get_endpoint_url(endpoint, endpoint_category)
        self._peek_message_out(
            "get", self._rest_session.headers, {}, url, params)
        response = self._rest_session.get(url, params=params)
        return self.handle_response(endpoint_category, response, parse_response)

    def post(self, endpoint: str, endpoint_category: EndpointCategory, json_data: Any, parse_response: ParseResponseFn[T], headers: dict = {}) -> T:
        url = self._get_endpoint_url(endpoint, endpoint_category)
        self._peek_message_out(
            "post", self._rest_session.headers, headers, url, json_data)
        response = self._rest_session.post(
            url, json=json_data, headers=headers)
        return self.handle_response(endpoint_category, response, parse_response)

    def delete(self, endpoint: str, endpoint_category: EndpointCategory, params: Any, parse_response: ParseResponseFn[T]) -> T:
        url = self._get_endpoint_url(endpoint, endpoint_category)
        self._peek_message_out(
            "delete", self._rest_session.headers, {}, url, params)
        response = self._rest_session.delete(url, json=params)
        return self.handle_response(endpoint_category, response, parse_response)

    def handle_response(self, endpoint_category: EndpointCategory,response : requests.Response, parse_response: ParseResponseFn[T]) -> T:
        self._peek_message_in(response.text)
        return ResponseHandler.handle_response(
            endpoint_category,
            parse_response,
            response)

    def authenticate_user(self, authenticate_request: AuthenticateRequest) -> AuthenticateResponse:
        request_data = Authenticator.convert_data(authenticate_request)
        headers = to_dict(request_data)
        self._rest_session.headers.update(headers)
        auth_response = self.get(
            AUTHENTICATE_USER_ENDPOINT,
            EndpointCategory.AP,
            {},
            lambda response_data: from_dict(AuthenticateResponse, response_data))
        if not auth_response.authenticated:
            raise NotbankException(
                ErrorCode.OPERATION_FAILED,
                auth_response.errormsg if auth_response.errormsg else "unable to authenticate")
        self._update_headers(ap_token=auth_response.session_token,
                             header_to_remove_list=list(headers.keys()))
        return auth_response
