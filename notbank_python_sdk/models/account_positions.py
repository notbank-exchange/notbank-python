from dataclasses import dataclass
from decimal import Decimal


@dataclass
class AccountPosition:
    oms_id: int
    account_id: int
    product_symbol: str
    product_id: int
    amount: Decimal
    hold: Decimal
    pending_deposits: Decimal
    pending_withdraws: Decimal
    total_day_deposits: Decimal
    total_month_deposits: Decimal
    total_year_deposits: Decimal
    total_day_deposit_notional: Decimal
    total_month_deposit_notional: Decimal
    total_year_deposit_notional: Decimal
    total_day_withdraws: Decimal
    total_month_withdraws: Decimal
    total_year_withdraws: Decimal
    total_day_withdraw_notional: Decimal
    total_month_withdraw_notional: Decimal
    total_year_withdraw_notional: Decimal
    notional_product_id: int
    notional_product_symbol: str
    notional_value: Decimal
    notional_hold_amount: Decimal
    notional_rate: Decimal
    total_day_transfer_notional: Decimal
