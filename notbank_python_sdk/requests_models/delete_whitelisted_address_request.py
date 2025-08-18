from dataclasses import dataclass
from typing import Union
from uuid import UUID


@dataclass
class DeleteWhiteListedAddressRequest:
    whitelisted_address_id: UUID
    account_id: int
    otp: str


@dataclass
class DeleteWhiteListedAddressRequestInternal:
    account_id: int
    otp: str
