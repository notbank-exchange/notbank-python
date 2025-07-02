from dataclasses import dataclass
from decimal import Decimal

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class ModifyOrderRequest(WithOMSId):
    order_id: int
    instrument_id: int
    quantity: Decimal
    account_id: int
