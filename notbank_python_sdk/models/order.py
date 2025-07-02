from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Order:
    side: str
    order_id: int
    price: Decimal
    quantity: Decimal
    display_quantity: Decimal
    instrument: int
    account: int
    account_name: str
    order_type: str
    client_order_id: int
    order_state: str
    receive_time: int
    receive_time_ticks: int
    last_updated_time: int
    last_updated_time_ticks: int
    orig_quantity: Decimal
    quantity_executed: Decimal
    gross_value_executed: Decimal
    executable_value: Decimal
    avg_price: Decimal
    counter_party_id: int
    change_reason: str
    orig_order_id: int
    orig_cl_ord_id: int
    entered_by: int
    user_name: str
    is_quote: bool
    inside_ask: Decimal
    inside_ask_size: Decimal
    inside_bid: Decimal
    inside_bid_size: Decimal
    last_trade_price: Decimal
    reject_reason: str
    is_locked_in: bool
    cancel_reason: str
    order_flag: str
    use_margin: bool
    stop_price: Decimal
    peg_price_type: str
    peg_offset: Decimal
    peg_limit_offset: Decimal
    oms_id: int
    ip_address: Optional[str] = None
    ipv6a: Optional[int] = None
    ipv6b: Optional[int] = None
    client_order_id_uuid: Optional[str] = None
