from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, IntEnum
from notbank_python_sdk.constants import MakerTaker, OrderType, Side

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetOrderFeeRequest(WithOMSId):
    account_id: int
    instrument_id: int
    quantity: Decimal
    price: Decimal
    order_type: OrderType
    maker_taker: MakerTaker
    side: Side
