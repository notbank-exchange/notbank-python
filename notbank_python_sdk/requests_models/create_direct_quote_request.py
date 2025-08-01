from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CreateDirectQuoteRequest:
    account_id: int
    from_currency: str
    from_amount: Decimal
    to_currency: str
    operation: str

