from dataclasses import dataclass
from typing import Optional


@dataclass
class UrlResponse:
    url: Optional[str] = None
