from dataclasses import dataclass

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetTickerHistoryRequest(WithOMSId):
    instrument_id: int
    interval: int
    from_date: str
    to_date: str
