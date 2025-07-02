from dataclasses import dataclass
from typing import List, Optional

from notbank_python_sdk.models.product_limit import ProductLimit


@dataclass
class VerificationLevelConfig:
    level: int
    oms_id: int
    products: List[ProductLimit]
    level_name: Optional[str] = None
