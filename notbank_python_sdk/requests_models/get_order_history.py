from dataclasses import dataclass
from typing import Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetOrderHistoryRequest(WithOMSId):
    account_id: int
    order_state: Optional[str] = None
    order_id: Optional[int] = None
    client_order_id: Optional[int] = None
    original_order_id: Optional[int] = None
    original_client_order_id: Optional[int] = None
    user_id: Optional[int] = None
    instrument_id: Optional[int] = None
    start_timestamp: Optional[int] = None
    end_timestamp: Optional[int] = None
    depth: Optional[int] = None
    limit: Optional[int] = None
    start_index: Optional[int] = None
