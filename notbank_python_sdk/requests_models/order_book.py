from dataclasses import dataclass
from typing import Optional


@dataclass
class OrderBookRequest:
    market_pair: str
    depth: Optional[int] = None
    level: Optional[int] = None
