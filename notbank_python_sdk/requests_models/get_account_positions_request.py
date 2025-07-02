from dataclasses import dataclass
from typing import Optional

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetAccountPositionsRequest(WithOMSId):
    account_id: int
    include_pending: Optional[bool] = None
