from dataclasses import dataclass
from enum import Enum


class Action(str, Enum):
    ENABLE = "enable"
    DISABLE = "disable"


@dataclass
class UpdateOneStepWithdrawRequest:
    account_id: int
    action: Action
    otp: str
