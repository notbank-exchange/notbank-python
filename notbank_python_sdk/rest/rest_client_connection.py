from typing import Any, Callable, Optional, TypeVar

import requests

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

    def __init__(self, host: str, ap_token: Optional[str] = None):
        self.host = self._get_host_url(host)
        self._rest_session = requests.Session()
        self._rest_session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': f'{self.NAME} Python SDK v{self.VERSION}',
        })
        self._update_headers(ap_token)
        self._two_factor_token: Optional[str] = None

    def _get_host_url(self, host: str) -> str:
        return "https://" + host

    def _update_headers(self, ap_token: Optional[str]) -> None:
        if ap_token is not None:
            self._rest_session.headers.update({
                'aptoken': ap_token,
            })

    def close(self) -> None:
        self._rest_session.close()

    def _get_endpoint_url(self, endpoint: str, endpoint_category: EndpointCategory,) -> str:
        url = self.host + "/" + endpoint_category + "/" + endpoint
        print(url)
        return url

    def get(self, endpoint: str, endpoint_category: EndpointCategory, params: Any, parse_response: ParseResponseFn[T]) -> T:
        response = self._rest_session.get(
            self._get_endpoint_url(endpoint, endpoint_category), params=params)
        return self.handle_response(endpoint_category, response, parse_response)

    def post(self, endpoint: str, endpoint_category: EndpointCategory, json_data: Any, parse_response: ParseResponseFn[T], headers: Optional[Any] = None) -> T:
        print("headers", self._rest_session.headers)
        response = self._rest_session.post(
            self._get_endpoint_url(endpoint, endpoint_category), json=json_data, headers=headers)
        return self.handle_response(endpoint_category, response, parse_response)

    def delete(self, endpoint: str, endpoint_category: EndpointCategory, params: Any, parse_response: ParseResponseFn[T]) -> T:
        response = self._rest_session.delete(
            self._get_endpoint_url(endpoint, endpoint_category))
        return self.handle_response(endpoint_category, response, parse_response)

    def handle_response(self, endpoint_category: EndpointCategory, response: requests.Response, parse_response: ParseResponseFn[T]) -> T:
        if response.status_code < 200 or 300 <= response.status_code:
            raise NotbankException(
                ErrorCode.CONFIGURATION_ERROR,
                f"http error. (code={response.status_code}) " + response.text)
        response_data = response.json()
        return ResponseHandler.handle_response_data(endpoint_category, parse_response, response_data)

    def authenticate_user(self, authenticate_request: AuthenticateRequest) -> AuthenticateResponse:
        request_data = Authenticator.convert_data(authenticate_request)
        self._rest_session.headers.update(to_dict(request_data))
        auth_response = self.get(
            AUTHENTICATE_USER_ENDPOINT,
            EndpointCategory.AP,
            {},
            lambda response_data: from_dict(AuthenticateResponse, response_data))
        self._rest_session.headers.clear()
        if auth_response.requires_2fa:
            self._two_factor_token = auth_response.two_fa_token

        self._update_headers(ap_token=auth_response.session_token)
        return auth_response
