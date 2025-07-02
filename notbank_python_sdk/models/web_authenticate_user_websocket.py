from dataclasses import dataclass
from typing import Optional


@dataclass
class WebAuthenticateUserResponse:
    authenticated: bool
    session_token: str
    user_id: str
    two_fa_token: Optional[str] = None
    requires_2fa: Optional[bool] = None
    auth_type: Optional[str] = None
    errormsg: Optional[str] = None
