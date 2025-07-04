from dataclasses import dataclass
from decimal import Decimal


@dataclass
class OmsFee:
    oms_id: int
    account_id: int
    account_provider_id: int
    fee_id: int
    fee_amt: Decimal
    fee_calc_type: str
    is_active: bool
    product_id: int
    minimal_fee_amt: Decimal
    minimal_fee_calc_type: str
