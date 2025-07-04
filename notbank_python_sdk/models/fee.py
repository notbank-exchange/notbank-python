from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Fee:
    fee_amount: Decimal
    ticket_amount: Decimal
