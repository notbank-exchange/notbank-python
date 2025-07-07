from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateCryptoWithdrawRequest:
    account_id: str
    currency: str
    network: str
    address: str
    amount: str
    memo_or_tag: Optional[str]
    otp: Optional[str]
