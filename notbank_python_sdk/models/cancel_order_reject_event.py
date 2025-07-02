

from dataclasses import dataclass


@dataclass
class CancelOrderRejectEvent:
    oms_id: int
    account_id: int
    order_id: int
    order_revision: int
    order_type: str
    instrument_id: int
    status: str
    reject_reason: str
