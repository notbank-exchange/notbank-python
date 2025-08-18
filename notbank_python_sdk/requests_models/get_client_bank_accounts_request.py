from dataclasses import dataclass
from typing import Optional


@dataclass
class GetClientBankAccountsRequest:
    page: Optional[int] = None
    page_size: Optional[int] = None
