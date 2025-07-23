from dataclasses import dataclass
from typing import Union
from uuid import UUID


@dataclass
class DeleteWhiteListedAddressRequest:
    whitelisted_address_id: UUID
    account_id: Union[int, str]
    otp: str


@dataclass
class DeleteWhiteListedAddressRequestInternal:
    account_id: str
    otp: str
