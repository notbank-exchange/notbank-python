from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetDepositFeeRequest(WithOMSId):
    account_id: int
    product_id: int
    amount: Decimal
    account_provider_id: Optional[int] = None
