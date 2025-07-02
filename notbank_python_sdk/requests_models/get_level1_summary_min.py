from dataclasses import dataclass
from typing import Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetLevel1SummaryMinRequest(WithOMSId):
    instrument_ids: Optional[str] = None
