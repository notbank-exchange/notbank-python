from dataclasses import dataclass
from typing import Optional


@dataclass
class Address:
    id: str
    currency: str
    label: str
    network: str
    address: str
    verified: bool
    provider_id: int
    memo: Optional[str] = None
