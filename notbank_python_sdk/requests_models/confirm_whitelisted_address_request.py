from dataclasses import dataclass
from typing import Union
from uuid import UUID


@dataclass
class ConfirmWhiteListedAddressRequest:
    whitelisted_address_id: UUID
    account_id: int
    sms_code: str


@dataclass
class ConfirmWhiteListedAddressRequestInternal:
    account_id: int
    sms_code: str
