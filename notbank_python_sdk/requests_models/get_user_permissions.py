from dataclasses import dataclass


@dataclass
class GetUserPermissionsRequest:
    user_id: int
