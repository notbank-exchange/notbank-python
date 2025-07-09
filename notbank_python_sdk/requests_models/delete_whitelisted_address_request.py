from dataclasses import dataclass
from typing import Union


@dataclass
class DeleteWhiteListedAddressRequest:
    whitelisted_address_id: str
    account_id: Union[int, str]
    otp: str


@dataclass
class DeleteWhiteListedAddressRequestInternal:
    account_id: str
    otp: str
