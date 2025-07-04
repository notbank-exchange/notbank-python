from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class ProductLimits:
    oms_id: int
    verification_level: int
    product_id: int
    product_name: str
    auto_withdraw_threshold: Decimal
    daily_deposit_limit: Decimal
    daily_deposit_notional_limit: Decimal
    monthly_deposit_limit: Decimal
    monthly_deposit_notional_limit: Decimal
    yearly_deposit_limit: Decimal
    yearly_deposit_notional_limit: Decimal
    daily_withdraw_limit: Decimal
    daily_withdraw_notional_limit: Decimal
    monthly_withdraw_limit: Decimal
    monthly_withdraw_notional_limit: Decimal
    yearly_withdraw_limit: Decimal
    yearly_withdraw_notional_limit: Decimal
    daily_transfer_notional_limit: Decimal
    notional_product_id: int
    over_limit_rejected: bool
    withdraw_processing_delay_sec: int
    deposit_ticket_workflow: str
    withdraw_ticket_workflow: str
    require_whitelisted_address: bool
    auto_accept_whitelisted_address: bool
    verification_level_name: Optional[str] = None
