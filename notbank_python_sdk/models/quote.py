from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass
class Quote:
    id: UUID
    is_inverse: bool
    type: int
    state: int
    currency_in: str
    currency_out: str
    amount_in: Decimal
    amount_out: Decimal
    amount_usdt_out: Decimal
    fee_amount: Decimal
    fee_detail: str
