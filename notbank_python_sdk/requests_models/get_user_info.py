from dataclasses import dataclass
from typing import Optional


@dataclass
class GetUserInfoRequest:
    user_id: Optional[int] = None
    email: Optional[str] = None
    username: Optional[str] = None
    affiliate_id: Optional[int] = None
