from dataclasses import dataclass
from uuid import UUID


@dataclass
class RegisterUserResponse:
    user_id: UUID
    token: str
