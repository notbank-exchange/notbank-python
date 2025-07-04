from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class InstrumentLimits:
    verification_level: int
    oms_id: int
    instrument_id: int
    instrument_name: str
    order_buy_limit: Decimal
    order_sell_limit: Decimal
    daily_buy_limit: Decimal
    daily_sell_limit: Decimal
    monthly_buy_limit: Decimal
    monthly_sell_limit: Decimal
    notional_product_id: int
    order_notional_limit: Decimal
    daily_notional_limit: Decimal
    monthly_notional_limit: Decimal
    yearly_notional_limit: Decimal
    verification_level_name: Optional[str] = None
