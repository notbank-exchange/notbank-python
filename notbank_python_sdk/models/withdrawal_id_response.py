from dataclasses import dataclass
from typing import Optional


@dataclass
class WithdrawalIdResponse:
    withdrawal_id: Optional[str] = None
