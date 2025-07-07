from dataclasses import dataclass
from typing import Optional


@dataclass
class Address:
    id: str
    currency: str
    label: str
    network: str
    address: str
    memo: Optional[str]
    verified: bool
