from dataclasses import dataclass


@dataclass
class AddWhitelistedAddressRequest:
    account_id: int
    currency: str
    network: str
    address: str
    label: str
    otp: str
