from dataclasses import dataclass
from typing import Union
from uuid import UUID


@dataclass
class ConfirmWhiteListedAddressRequest:
    whitelisted_address_id: UUID
    code: str


@dataclass
class ConfirmWhiteListedAddressRequestInternal:
    code: str
