from dataclasses import dataclass
from typing import Optional


@dataclass
class GetWhitelistedAddressesRequest:
    account_id: str
    search: Optional[str] = None
