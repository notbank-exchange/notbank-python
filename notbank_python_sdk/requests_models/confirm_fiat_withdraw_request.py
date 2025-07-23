from dataclasses import dataclass
from uuid import UUID


@dataclass
class ConfirmFiatWithdrawRequest:
    withdrawal_id: UUID
    attempt_code: str


@dataclass
class ConfirmFiatWithdrawRequestInternal:
    attempt_code: str
