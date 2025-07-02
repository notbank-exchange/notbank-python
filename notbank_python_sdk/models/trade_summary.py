from dataclasses import dataclass
from decimal import Decimal


@dataclass
class TradeSummary:
    trade_id: int
    price: Decimal
    base_volume: Decimal
    quote_volume: Decimal
    timestamp: str
    type: str
