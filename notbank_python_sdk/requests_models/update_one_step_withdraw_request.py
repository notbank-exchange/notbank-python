from dataclasses import dataclass
from enum import Enum

from notbank_python_sdk.constants import UpdateOneStepWithdrawAction


@dataclass
class UpdateOneStepWithdrawRequest:
    account_id: int
    action: UpdateOneStepWithdrawAction
    otp: str
