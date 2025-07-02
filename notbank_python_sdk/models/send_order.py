from dataclasses import dataclass
from enum import Enum
from typing import Optional


class SendOrderStatus(str, Enum):
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"


@dataclass
class SendOrderResponse:
    status: SendOrderStatus
    order_id: Optional[int] = None
    errormsg: Optional[str] = None
