from dataclasses import dataclass
from typing import Union


@dataclass
class ConfirmWhiteListedAddressRequest:
    whitelisted_address_id: str
    code: str


@dataclass
class ConfirmWhiteListedAddressRequestInternal:
    code: str
