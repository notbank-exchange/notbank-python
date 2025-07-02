from dataclasses import dataclass
from decimal import Decimal


@dataclass
class InstrumentStatistic:
    oms_id: int
    account_id: int
    instrument_id: int
    instrument_symbol: str
    quantity_bought: Decimal
    quantity_sold: Decimal
    notional_bought: Decimal
    notional_sold: Decimal
    monthly_quantity_bought: Decimal
    monthly_quantity_sold: Decimal
    monthly_notional_bought: Decimal
    monthly_notional_sold: Decimal
    trade_volume: Decimal
    monthly_trade_volume: Decimal
    total_day_buys: int
    total_day_sells: int
    total_month_buys: int
    total_month_sells: int
    notional_conversion_rate: Decimal
    notional_conversion_symbol: str
    rolling_monthly_start_date: int
    last_trade_id: int
    daily_notional_trade_volume: Decimal
    monthly_notional_trade_volume: Decimal
    yearly_notional_trade_volume: Decimal
