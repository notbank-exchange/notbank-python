from dataclasses import dataclass


@dataclass
class DepositAddressRequest:
    account_id: str
    currency: str
    network: str
