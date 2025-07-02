from dataclasses import dataclass
from typing import Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class UnsubscribeLevel2Request(WithOMSId):
    instrument_id: Optional[int] = None
    symbol: Optional[str] = None
