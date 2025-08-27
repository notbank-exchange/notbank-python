from typing import Any, Callable, Optional

from notbank_python_sdk.client_connection import ClientConnection
from notbank_python_sdk.rest.rest_client_connection import RestClientConnection
from notbank_python_sdk.websocket.connection_configuration import ConnectionConfiguration
from notbank_python_sdk.websocket.websocket_connection import WebsocketConnection
from notbank_python_sdk.websocket.websocket_restarter.restarter import Restarter
from notbank_python_sdk.websocket.websocket_restarter.restarting_websocket_connection import RestartingWebsocketConnection


def _get_not_implemented(method_name: str, client_name: str) -> Callable[..., None]:
    def _not_implemented(*args: Any, **kwargs: Any) -> None:
        raise NotImplementedError(
            f"{method_name} is not implemented in {client_name}.")
    return _not_implemented


API_NOTBANK_EXCHANGE = "api.notbank.exchange"


def new_websocket_client_connection(
    url: str = API_NOTBANK_EXCHANGE,
    on_open: Callable[[], None] = lambda: None,
    on_close: Callable[[Any, str], None] = lambda code, message: None,
    on_failure: Callable[[Exception], None] = lambda e: None,
    peek_message_in: Callable[[str], None] = lambda x: None,
    peek_message_out: Callable[[str], None] = lambda x: None,
    request_timeout: Optional[float] = None,
) -> ClientConnection:
    client_restarter = WebsocketConnection.create(
        url, on_open, on_close, on_failure, peek_message_in, peek_message_out, request_timeout)
    return ClientConnection(
        post_request=client_restarter.request,
        get_request=client_restarter.request,
        delete_request=_get_not_implemented(
            "delete request", "WebsocketClientConnection"),
        subscribe=client_restarter.subscribe,
        unsubscribe=client_restarter.unsubscribe,
        authenticate_user=lambda request_message: client_restarter.authenticate_user(
            request_message),
        connect=client_restarter.connect,
        close=client_restarter.close,
    )


def new_restarting_websocket_client_connection(
    url: str = API_NOTBANK_EXCHANGE,
    on_open: Callable[[], None] = lambda: None,
    on_close: Callable[[Any, str], None] = lambda code, message: None,
    on_failure: Callable[[Exception], None] = lambda e: None,
    peek_message_in: Callable[[str], None] = lambda x: None,
    peek_message_out: Callable[[str], None] = lambda x: None,
    request_timeout: Optional[float] = None,
) -> ClientConnection:
    restarter = Restarter.create(
        ConnectionConfiguration(
            url, on_open, on_close, on_failure, peek_message_in, peek_message_out, request_timeout)
    )
    restarting_websocket_connection = RestartingWebsocketConnection(restarter)
    return ClientConnection(
        post_request=restarting_websocket_connection.request,
        get_request=restarting_websocket_connection.request,
        delete_request=_get_not_implemented(
            "delete request", "WebsocketClientConnection"),
        subscribe=restarting_websocket_connection.subscribe,
        unsubscribe=restarting_websocket_connection.unsubscribe,
        authenticate_user=restarting_websocket_connection.authenticate_user,
        connect=restarting_websocket_connection.connect,
        close=restarting_websocket_connection.close,
    )


def new_rest_client_connection(
    url: str = API_NOTBANK_EXCHANGE,
    peek_message_in: Callable[[str], None] = lambda a: None,
    peek_message_out: Callable[[str, Any, Any, str,
                                dict], None] = lambda a, b, c, d, e: None,
) -> ClientConnection:
    rest_client_connection = RestClientConnection(
        url, peek_message_in=peek_message_in, peek_message_out=peek_message_out)
    return ClientConnection(
        post_request=rest_client_connection.post,
        get_request=rest_client_connection.get,
        delete_request=rest_client_connection.delete,
        subscribe=_get_not_implemented("subscription", "RestClientConnection"),
        unsubscribe=_get_not_implemented(
            "unsubscription", "RestClientConnection"),
        authenticate_user=rest_client_connection.authenticate_user,
        connect=_get_not_implemented("connect", "RestClientConnection"),
        close=rest_client_connection.close,
    )
