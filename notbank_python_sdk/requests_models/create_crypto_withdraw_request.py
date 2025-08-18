from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class CreateCryptoWithdrawRequest:
    account_id: int
    currency: str
    network: str
    address: str
    amount: Decimal
    memo_or_tag: Optional[str] = None
    otp: Optional[str] = None
