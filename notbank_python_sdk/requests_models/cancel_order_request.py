from typing import Optional
from dataclasses import dataclass

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class CancelOrderRequest(WithOMSId):
    account_id: Optional[int] = None
    order_id: Optional[int] = None
    cl_order_id: Optional[int] = None
