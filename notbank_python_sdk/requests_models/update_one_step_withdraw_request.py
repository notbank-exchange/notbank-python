from dataclasses import dataclass


@dataclass
class UpdateOneStepWithdrawRequest:
    action: str
    otp: str
