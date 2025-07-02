from typing import Optional
from dataclasses import dataclass

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class CancelAllOrdersRequest(WithOMSId):
    account_id: Optional[int] = None
    instrument_id: Optional[int] = None
