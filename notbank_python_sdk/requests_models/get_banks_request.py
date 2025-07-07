from dataclasses import dataclass
from typing import Optional


@dataclass
class GetBanksRequest:
    country: str
    page: Optional[int] = None
    page_size: Optional[int] = None
