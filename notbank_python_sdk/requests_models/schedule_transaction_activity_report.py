from dataclasses import dataclass
from typing import List, Optional, Union

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class ScheduleTransactionActivityReportRequest(WithOMSId):
    begin_time: str
    account_id_list: List[int]
    frequency: Optional[Union[int, str]] = None
