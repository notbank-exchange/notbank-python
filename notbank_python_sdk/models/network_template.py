from dataclasses import dataclass
from typing import Optional


@dataclass
class NetworkTemplate:
    name: str
    type: str
    required: bool
    max_length: Optional[int] = None
    min_length: Optional[int] = None
