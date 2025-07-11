from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateBankAccountRequest:
    country: str
    bank: str
    number: str
    kind: str
    pix_type: Optional[str] = None
    agency: Optional[str] = None
    dv: Optional[str] = None
    province: Optional[str] = None
