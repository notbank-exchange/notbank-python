from dataclasses import dataclass
from typing import Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class UnsubscribeOrderStateEventsRequest(WithOMSId):
    account_id: int
    instrument_id: Optional[int] = None
