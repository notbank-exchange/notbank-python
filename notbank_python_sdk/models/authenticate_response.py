from dataclasses import dataclass
from typing import Optional

from notbank_python_sdk.models.user import User as AUser


@dataclass
class AuthenticateResponse:
    authenticated: bool
    requires_2fa: Optional[bool] = None
    two_fa_type: Optional[str] = None
    two_fa_token: Optional[str] = None
    locked: Optional[bool] = None
    user: Optional[AUser] = None
    errormsg: Optional[str] = None
    session_token: Optional[str] = None
    enforce_enable_2fa: Optional[bool] = None
    pending2_fa_token: Optional[str] = None
