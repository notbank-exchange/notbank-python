from dataclasses import dataclass
from typing import Optional


@dataclass
class WebAuthenticateUser:
    authenticated: bool
    session_token: Optional[str] = None
    user_id: Optional[str] = None
    two_fa_token: Optional[str] = None
    requires_2fa: Optional[bool] = None
    auth_type: Optional[str] = None
    errormsg: Optional[str] = None
