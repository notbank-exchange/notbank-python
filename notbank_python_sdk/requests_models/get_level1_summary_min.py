from dataclasses import dataclass
from typing import List, Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetLevel1SummaryMinRequest(WithOMSId):
    instrument_ids: Optional[List[int]] = None

@dataclass
class GetLevel1SummaryMinRequestInternal(WithOMSId):
    instrument_ids: Optional[str] = None
