from dataclasses import dataclass
from uuid import UUID


@dataclass
class IdResponse:
    id: UUID
