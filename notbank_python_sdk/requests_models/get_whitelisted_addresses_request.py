from dataclasses import dataclass
from typing import Optional


@dataclass
class GetWhitelistedAddressesRequest:
    account_id: int
    search: Optional[str] = None
