from dataclasses import dataclass

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetLevel1Request(WithOMSId):
    instrument_id: int
