
from dataclasses import dataclass


@dataclass
class GetDepositAddressRequest:
    account_id: str
    currency: str
    network: str
