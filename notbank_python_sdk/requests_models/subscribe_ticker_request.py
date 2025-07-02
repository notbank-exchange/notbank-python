from dataclasses import dataclass

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class SubscribeTickerRequest(WithOMSId):
    instrument_id: int
    interval: int
    include_last_count: int
