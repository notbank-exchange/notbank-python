from dataclasses import dataclass
from decimal import Decimal


@dataclass
class InstrumentSummary:
    trading_pairs: str
    last_price: Decimal
    lowest_ask: Decimal
    highest_bid: Decimal
    base_volume: Decimal
    quote_volume: Decimal
    price_change_percent_24h: Decimal
    highest_price_24h: Decimal
    lowest_price_24h: Decimal
