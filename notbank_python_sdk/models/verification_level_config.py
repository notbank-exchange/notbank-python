from dataclasses import dataclass
from typing import List, Optional
from notbank_python_sdk.models.instrument_limits import InstrumentLimits

from notbank_python_sdk.models.product_limits import ProductLimits


@dataclass
class ProductVerificationLevelConfig:
    level: int
    oms_id: int
    products: List[ProductLimits]
    level_name: Optional[str] = None


@dataclass
class InstrumentVerificationLevelConfig:
    level: int
    oms_id: int
    instruments: List[InstrumentLimits]
    level_name: Optional[str] = None
