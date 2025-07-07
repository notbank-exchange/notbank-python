from dataclasses import dataclass
from typing import List


@dataclass
class Bank:
    id: str
    name: str
    country: str


@dataclass
class Banks:
    total: int
    data: List[Bank]
