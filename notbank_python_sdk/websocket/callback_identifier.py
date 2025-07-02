import json
from typing import Callable, Optional, Dict, Union
from notbank_python_sdk.core.endpoints import WebSocketEndpoint

from notbank_python_sdk.websocket.message_frame import MessageFrame


class CallbackIdentifier:
    _mapping: Dict[WebSocketEndpoint, Callable[[str, str], str]] = {
        WebSocketEndpoint.SUBSCRIBE_LEVEL_1: lambda event_name, payload: CallbackIdentifier._get_level1_ticker_name(event_name, payload),
        WebSocketEndpoint.UPDATE_LEVEL_1: lambda event_name, payload: CallbackIdentifier._get_level1_ticker_name(event_name, payload),
        WebSocketEndpoint.SUBSCRIBE_LEVEL_2: lambda event_name, payload: CallbackIdentifier._get_level2_ticker_name(event_name, payload),
        WebSocketEndpoint.UPDATE_LEVEL_2: lambda event_name, payload: CallbackIdentifier._get_level2_ticker_name(event_name, payload),
        WebSocketEndpoint.SUBSCRIBE_TICKER: lambda event_name, payload: CallbackIdentifier._get_ticker_name(event_name, payload),
        WebSocketEndpoint.UPDATE_TICKER: lambda event_name, payload: CallbackIdentifier._get_ticker_name(event_name, payload),
        WebSocketEndpoint.SUBSCRIBE_TRADES: lambda event_name, payload: CallbackIdentifier._get_socket_trade_name(event_name, payload),
        WebSocketEndpoint.SUBSCRIBE_ORDER_STATE_EVENTS: lambda event_name, payload: CallbackIdentifier._get_order_event_name(event_name, payload),
        WebSocketEndpoint.ACCOUNT_EVENT_TRANSACTION: lambda event_name, payload: CallbackIdentifier._get_account_event_name(event_name, payload),
        WebSocketEndpoint.ACCOUNT_EVENT_WITHDRAW_TICKET_UPDATE: lambda event_name, payload: CallbackIdentifier._get_account_event_name(event_name, payload),
        WebSocketEndpoint.ACCOUNT_EVENT_ACCOUNT_POSITION: lambda event_name, payload: CallbackIdentifier._get_account_event_name(event_name, payload),
        WebSocketEndpoint.ACCOUNT_EVENT_ORDER_TRADE: lambda event_name, payload: CallbackIdentifier._get_account_event_name(event_name, payload),
        WebSocketEndpoint.ACCOUNT_EVENT_ORDER_STATE: lambda event_name, payload: CallbackIdentifier._get_account_event_name(event_name, payload),
        WebSocketEndpoint.ACCOUNT_EVENT_DEPOSIT_TICKET_UPDATE: lambda event_name, payload: CallbackIdentifier._get_account_event_name(event_name, payload),
        WebSocketEndpoint.ACCOUNT_EVENT_ACCOUNT_INFO_UPDATE: lambda event_name, payload: CallbackIdentifier._get_account_event_name(event_name, payload),
        WebSocketEndpoint.ACCOUNT_EVENT_CANCEL_ORDER_REJECT: lambda event_name, payload: CallbackIdentifier._get_account_event_name(event_name, payload),
        WebSocketEndpoint.ACCOUNT_EVENT_DEPOSIT: lambda event_name, payload: CallbackIdentifier._get_account_event_name(event_name, payload),
    }

    @staticmethod
    def get(event_name: str, first_identifier: Optional[int] = None, second_identifier: Optional[int] = None) -> str:
        return event_name + CallbackIdentifier._get_id_chunk(first_identifier) + CallbackIdentifier._get_id_chunk(second_identifier)

    @staticmethod
    def get_from_message_frame(message: MessageFrame) -> Optional[str]:
        try:
            websocket_endpoint = WebSocketEndpoint(message.n)
        except ValueError as e:
            return None
        mapping_function = CallbackIdentifier._mapping.get(websocket_endpoint)
        return mapping_function(message.n, message.o) if mapping_function else message.n

    @staticmethod
    def _get_ticker_name(event_name: str, payload_str: str) -> str:
        instrument_id = CallbackIdentifier._get_value_from_list(
            payload_str, 8)
        return event_name + CallbackIdentifier._get_id_chunk(instrument_id)

    @staticmethod
    def _get_level1_ticker_name(event_name: str, payload_str: str) -> str:
        instrument_id = CallbackIdentifier._get_instrumented_id(
            payload_str)
        return event_name + CallbackIdentifier._get_id_chunk(instrument_id)

    @staticmethod
    def _get_level2_ticker_name(event_name: str, payload_str: str) -> str:
        data = json.loads(payload_str)
        if not data or len(data) < 1 or len(data[0]) < 8:
            return event_name
        level2_ticker = data[0]
        instrument_id = level2_ticker[7]
        return event_name + CallbackIdentifier._get_id_chunk(instrument_id)

    @staticmethod
    def _get_socket_trade_name(event_name: str, payload_str: str) -> str:
        instrument_id = CallbackIdentifier._get_value_from_list(
            payload_str, 1)
        return event_name + CallbackIdentifier._get_id_chunk(instrument_id)

    @staticmethod
    def _get_account_event_name(event_name: str, payload_str: str) -> str:
        account_id = CallbackIdentifier._get_account_id(
            payload_str) or CallbackIdentifier._get_account_id_from_account(payload_str)
        return event_name + CallbackIdentifier._get_id_chunk(account_id)

    @staticmethod
    def _get_order_event_name(event_name: str, payload_str: str) -> str:
        instrument_id = CallbackIdentifier._get_instrumented_id_from_instrument(
            payload_str)
        return event_name + CallbackIdentifier._get_id_chunk(instrument_id)

    @staticmethod
    def _get_id_chunk(identifier: Optional[Union[int, str]]) -> str:
        return f"_{identifier}" if identifier is not None else ""

    @staticmethod
    def _get_value_from_list(payload_str: str, index: int) -> Optional[str]:
        data = json.loads(payload_str)
        return data[0][index] if data else None

    @staticmethod
    def _get_instrumented_id(payload_str: str) -> str:
        data = json.loads(payload_str)
        return data.get("InstrumentId")

    @staticmethod
    def _get_instrumented_id_from_instrument(payload_str: str) -> Optional[str]:
        data = json.loads(payload_str)
        return data.get("Instrument")

    @staticmethod
    def _get_account_id(payload_str: str) -> Optional[str]:
        data = json.loads(payload_str)
        return data.get("AccountId")

    @staticmethod
    def _get_account_id_from_account(payload_str: str) -> Optional[str]:
        data = json.loads(payload_str)
        return data.get("Account")
