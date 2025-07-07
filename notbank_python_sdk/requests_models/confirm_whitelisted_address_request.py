from dataclasses import dataclass


@dataclass
class WhiteListedAddressRequest:
    whitelisted_address_id: str
