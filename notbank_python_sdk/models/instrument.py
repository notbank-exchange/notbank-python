from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Instrument:
    oms_id: int
    instrument_id: int
    symbol: str
    product1: int
    product1_symbol: str
    product2: int
    product2_symbol: str
    instrument_type: str
    venue_instrument_id: int
    venue_id: int
    sort_index: int
    session_status: str
    previous_session_status: str
    session_status_date_time: str
    self_trade_prevention: bool
    quantity_increment: Decimal
    price_increment: Decimal
    minimum_quantity: Decimal
    minimum_price: Decimal
    venue_symbol: str
    is_disable: bool
    master_data_id: int
    price_collar_threshold: Decimal
    price_collar_percent: Decimal
    price_collar_enabled: bool
    price_floor_limit: Decimal
    price_floor_limit_enabled: bool
    price_ceiling_limit: Decimal
    price_ceiling_limit_enabled: bool
    create_with_market_running: bool
    allow_only_market_maker_counter_party: bool
    price_collar_index_difference: Decimal
    price_collar_convert_to_otc_enabled: bool
    price_collar_convert_to_otc_client_user_id: int
    price_collar_convert_to_otc_account_id: int
    price_collar_convert_to_otc_threshold: Decimal
    otc_convert_size_enabled: bool
    otc_convert_size_threshold: Decimal
    otc_trades_public: bool
    price_tier: int
