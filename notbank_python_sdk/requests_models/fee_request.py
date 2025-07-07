from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class FeeRequest(WithOMSId):
    account_id: Optional[int] = None
    product_id: Optional[int] = None
    amount: Optional[Decimal] = None
    account_provider_id: Optional[int] = None
