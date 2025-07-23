from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from uuid import UUID


@dataclass
class CreateFiatDepositRequest:
    account_id: int
    payment_method: int
    currency: str
    amount: Decimal
    bank_account_id: Optional[UUID] = None
    voucher: Optional[str] = None
