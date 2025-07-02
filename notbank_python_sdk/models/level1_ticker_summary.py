from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Level1TickerSummary:
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
    current_day_notional: Decimal
    current_day_num_trades: int
    current_day_px_change: Decimal
    rolling_24_hr_volume: Decimal
    rolling_24_hr_notional: Decimal
    rolling_24_num_trades: int
    rolling_24_hr_px_change: Decimal
    time_stamp: str
    bid_qty: Decimal
    ask_qty: Decimal
    bid_order_ct: int
    ask_order_ct: int
    rolling_24_hr_px_change_percent: Decimal
