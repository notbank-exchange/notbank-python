from dataclasses import dataclass
from typing import Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetLastTradesRequest(WithOMSId):
    instrument_id: int
    count: Optional[int] = 100
