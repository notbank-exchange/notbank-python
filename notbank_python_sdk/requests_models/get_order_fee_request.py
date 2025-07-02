from dataclasses import dataclass
from decimal import Decimal

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetOrderFeeRequest(WithOMSId):
    account_id: int
    instrument_id: int
    quantity: Decimal
    price: Decimal
    order_type: int
    maker_taker: int
    side: int
