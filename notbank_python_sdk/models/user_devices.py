from dataclasses import dataclass


@dataclass
class UserDevice:
    hash_code: int
    location: str
    device_name: str
    ip_address: str
    user_id: int
    is_trusted: bool
    expiration_time: int
