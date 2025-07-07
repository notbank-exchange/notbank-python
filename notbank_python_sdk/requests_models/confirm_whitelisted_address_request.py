
from dataclasses import dataclass


@dataclass
class ConfirmWhiteListedAddressRequest:
    whitelisted_address_id: str
