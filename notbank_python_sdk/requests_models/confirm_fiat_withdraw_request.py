from dataclasses import dataclass


@dataclass
class ConfirmFiatWithdrawRequest:
    withdrawal_id: str
    attempt_code: str


@dataclass
class ConfirmFiatWithdrawRequestInternal:
    attempt_code: str
