from dataclasses import dataclass
from decimal import Decimal


@dataclass
class OrderFee:
    order_fee: Decimal
    product_id: int
