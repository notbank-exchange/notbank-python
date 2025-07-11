from dataclasses import dataclass
from typing import Union


@dataclass
class DepositAddressRequest:
    account_id: int
    currency: str
    network: str
