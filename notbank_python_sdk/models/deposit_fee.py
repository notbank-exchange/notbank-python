from dataclasses import dataclass
from decimal import Decimal


@dataclass
class DepositFee:
    fee_amount: Decimal
    ticket_amount: Decimal
