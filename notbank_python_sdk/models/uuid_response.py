from dataclasses import dataclass
from uuid import UUID


@dataclass
class UuidResponse:
    id: UUID
