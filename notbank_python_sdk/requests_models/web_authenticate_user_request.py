from dataclasses import dataclass
from typing import Optional


@dataclass
class WebAuthenticateUserRequest:
    session_token: Optional[str] = None
    jwt: Optional[str] = None
