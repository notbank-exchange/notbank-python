from dataclasses import dataclass
from typing import Optional


@dataclass
class GetTransactionsRequest:
    from_date: Optional[str] = None
    to_date: Optional[str] = None
    sort: Optional[str] = None
    currency: Optional[str] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
