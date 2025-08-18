from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CreateInverseQuoteRequest:
    account_id: int
    from_currency: str
    to_currency: str
    to_amount: Decimal

