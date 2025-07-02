from dataclasses import dataclass
from typing import List, Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class ScheduleTradeActivityReportRequest(WithOMSId):
    begin_time: str
    account_id_list: List[int]
    frequency: Optional[str] = None
