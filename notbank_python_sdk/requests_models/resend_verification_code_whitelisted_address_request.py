from dataclasses import dataclass
from typing import Union
from uuid import UUID


@dataclass
class ResendVerificationCodeWhitelistedAddressRequest:
    whitelisted_address_id: UUID
    account_id: int


@dataclass
class ResendVerificationCodeWhitelistedAddressInternal:
    account_id: int
