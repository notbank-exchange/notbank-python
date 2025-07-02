
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class DepositEvent:
    oms_id: int
    account_id: int
    product_id: int
    quantity: Decimal
    sub_account_id: int
