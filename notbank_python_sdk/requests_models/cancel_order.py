from dataclasses import dataclass

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class CancelOrder(WithOMSId):
    order_id: int
    account_id: int
