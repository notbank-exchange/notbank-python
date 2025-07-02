from dataclasses import dataclass
from typing import Optional


@dataclass
class GetUserDevicesRequest:
    user_id: Optional[int] = None
