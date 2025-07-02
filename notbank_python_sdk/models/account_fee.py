from dataclasses import dataclass
from decimal import Decimal


@dataclass
class AccountFee:
    fee_id: int
    oms_id: int
    fee_tier: int
    account_id: int
    fee_amt: Decimal
    fee_calc_type: str
    fee_type: str
    ladder_threshold: Decimal
    ladder_seconds: int
    is_active: bool
    instrument_id: int
    order_type: str
    pegged_product_id: int
