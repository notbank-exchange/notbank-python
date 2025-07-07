from dataclasses import dataclass
from typing import Optional


@dataclass
class GetNetworksTemplatesRequest:
    currency: str
    network: Optional[str]
