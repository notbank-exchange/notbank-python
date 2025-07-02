from dataclasses import dataclass


@dataclass
class Authenticate2FAResponse:
    authenticated: bool
    user_id: int
    session_token: str
