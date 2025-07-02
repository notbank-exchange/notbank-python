from dataclasses import dataclass

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class UnsubscribeAccountEventsRequest(WithOMSId):
    account_id: int
