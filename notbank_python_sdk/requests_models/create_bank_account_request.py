from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateBankAccountRequest:
    country: str
    bank: str
    number: str
    kind: str
    pix_type: Optional[str]
    agency: Optional[str]
    dv: Optional[str]
    province: Optional[str]
