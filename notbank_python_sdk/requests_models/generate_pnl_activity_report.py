from dataclasses import dataclass
from typing import List

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GeneratePnlActivityReportRequest(WithOMSId):
    start_time: str
    end_time: str
    account_id_list: List[int]
