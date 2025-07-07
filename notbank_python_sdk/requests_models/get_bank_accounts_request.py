from dataclasses import dataclass
from typing import Optional


@dataclass
class GetBankAccountsRequest:
    page: Optional[int] = None
    page_size: Optional[int] = None
