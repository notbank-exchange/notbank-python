from typing import Callable, Optional, TypeVar
from notbank_python_sdk.models.authenticate_response import AuthenticateResponse
from notbank_python_sdk.websocket.websocket_connection import WebsocketConnection

T = TypeVar('T')


class Reauther:
    _reauthenticate_connection: Callable[[
        WebsocketConnection], Optional[AuthenticateResponse]]

    def __init__(self):
        self._reauthenticate_connection = lambda x: None

    def update_authenticate_fn(self, authenticate_connection: Callable[[WebsocketConnection], Optional[AuthenticateResponse]]):
        self._reauthenticate_connection = authenticate_connection

    def reauthenticate(self, connection: WebsocketConnection) -> Optional[AuthenticateResponse]:
        return self._reauthenticate_connection(connection)
