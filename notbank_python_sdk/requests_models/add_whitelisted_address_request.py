
from dataclasses import dataclass


@dataclass
class AddWhitelistedAddressRequest:
    account_id: str
    currency: str
    network: str
    address: str
    label: str
    otp: str
