from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Union

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class SetOmsWithdrawFeeRequest(WithOMSId):
    product_id: int
    account_id: Optional[int] = None
    account_provider_id: Optional[int] = None
    fee_amt: Optional[Decimal] = None
    fee_calc_type: Optional[Union[str, int]] = None
    is_active: Optional[bool] = None
    minimal_fee_amt: Optional[Decimal] = None
    minimal_fee_calc_type: Optional[Union[str, int]] = None
