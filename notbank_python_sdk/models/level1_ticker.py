from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Level1Ticker:
    oms_id: int
    instrument_id: int
    best_bid: Decimal
    best_offer: Decimal
    last_traded_px: Decimal
    last_traded_qty: Decimal
    last_trade_time: int
    session_open: Decimal
    session_high: Decimal
    session_low: Decimal
    session_close: Decimal
    volume: Decimal
    current_day_volume: Decimal
    current_day_num_trades: int
    current_day_px_change: Decimal
    rolling24hr_notional: Decimal
    rolling24hr_volume: Decimal
    rolling24num_trades: int
    rolling24hr_px_change: Decimal
    time_stamp: str
    current_notional: Optional[Decimal] = None
