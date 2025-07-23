from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class CreateFiatWithdrawRequest:
    account_id: str
    payment_method: int
    currency: int
    amount: Decimal
    bank_account_id: Optional[str] = None
    cbu: Optional[str] = None
    person_type: Optional[str] = None
    cuit: Optional[str] = None
    name: Optional[str] = None
