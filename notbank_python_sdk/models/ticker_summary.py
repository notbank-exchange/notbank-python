from dataclasses import dataclass
from decimal import Decimal


@dataclass
class TickerSummary:
    base_id: int
    quote_id: int
    last_price: Decimal
    base_volume: Decimal
    quote_volume: Decimal
