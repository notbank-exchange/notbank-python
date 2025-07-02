from dataclasses import dataclass
from decimal import Decimal


@dataclass
class GetWithdrawFeeResponse:
    """
    Respuesta con el fee estimado para el retiro.
    """
    fee_amount: Decimal
    ticket_amount: Decimal
