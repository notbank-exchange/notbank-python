from dataclasses import dataclass
from typing import List
from uuid import UUID


@dataclass
class Bank:
    id: UUID
    name: str
    country: str


@dataclass
class Banks:
    total: int
    data: List[Bank]
