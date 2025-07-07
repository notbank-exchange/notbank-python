from typing import Any, Callable, Optional

from notbank_python_sdk.client_connection import ClientConnection
from notbank_python_sdk.rest.rest_client_connection import RestClientConnection
from notbank_python_sdk.websocket.restarter import ConnectionData, WebsocketClientRestarter
from notbank_python_sdk.websocket.websocket_client_connection import WebsocketClientConnection


def _get_not_implemented(method_name: str, client_name: str) -> Callable[..., None]:
    def _not_implemented(*args: Any, **kwargs: Any) -> None:
        raise NotImplementedError(
            f"{method_name} is not implemented in {client_name}.")
    return _not_implemented


def new_websocket_client_connection(
    url: str = "api.notbank.exchange",
    on_open: Callable[[], None] = lambda: None,
    on_close: Callable[[Any, str], None] = lambda code, message: None,
    on_failure: Callable[[Exception], None] = lambda e: None,
    peek_message_in: Callable[[str], None] = lambda x: None,
    peek_message_out: Callable[[str], None] = lambda x: None,
    request_timeout: Optional[float] = None,
) -> ClientConnection:
    client_restarter = WebsocketClientRestarter.create(
        ConnectionData(
            url, on_open, lambda: None, on_close, on_failure, peek_message_in, peek_message_out, request_timeout),
        10
    )
    return ClientConnection(
        post_request=lambda endpoint, endpoint_category, request_message, parse_response: client_restarter.get_connection(
        ).request(endpoint, endpoint_category, request_message, parse_response),
        get_request=lambda endpoint, endpoint_category, request_message, parse_response: client_restarter.get_connection(
        ).request(endpoint, endpoint_category, request_message, parse_response),
        delete_request=_get_not_implemented(
            "delete request", "WebsocketClientConnection"),
        subscribe=client_restarter.subscribe,
        unsubscribe=client_restarter.unsubscribe,
        authenticate_user=lambda request_message: client_restarter.get_connection(
        ).authenticate_user(request_message),
        connect=client_restarter.get_connection().connect,
        close=client_restarter.close,
    )


def new_rest_client_connection(url: str = "api.notbank.exchange") -> ClientConnection:

    rest_client_connection = RestClientConnection(url)
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
