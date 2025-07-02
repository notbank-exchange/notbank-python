from dataclasses import dataclass
from decimal import Decimal


@dataclass
class AccountTrade:
    oms_id: int
    execution_id: int
    trade_id: int
    order_id: int
    account_id: int
    account_name: str
    sub_account_id: int
    client_order_id: int
    instrument_id: int
    side: str
    order_type: str
    quantity: Decimal
    remaining_quantity: Decimal
    price: Decimal
    value: Decimal
    counter_party: str
    order_trade_revision: int
    direction: str
    is_block_trade: bool
    fee: Decimal
    fee_product_id: int
    order_originator: int
    user_name: str
    trade_time_ms: int
    maker_taker: str
    adapter_trade_id: int
    inside_bid: Decimal
    inside_bid_size: Decimal
    inside_ask: Decimal
    inside_ask_size: Decimal
    counter_party_client_user_id: int
    notional_product_id: int
    notional_rate: Decimal
    notional_value: Decimal
    trade_time: int
