from typing import Optional


class NetworkTemplate:
    name: str
    type: str
    required: bool
    max_length: Optional[int]
    min_length: Optional[int]
