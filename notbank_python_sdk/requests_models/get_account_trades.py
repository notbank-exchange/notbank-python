from dataclasses import dataclass
from typing import Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetAccountTradesRequest(WithOMSId):
    account_id: Optional[int] = None
    depth: Optional[int] = None
    start_index: Optional[int] = None
    instrument_id: Optional[int] = None
    trade_id: Optional[int] = None
    order_id: Optional[int] = None
    start_time_stamp: Optional[int] = None
    end_time_stamp: Optional[int] = None
    execution_id: Optional[int] = None
