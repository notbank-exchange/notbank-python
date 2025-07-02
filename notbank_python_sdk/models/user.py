from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    user_name: str
    email: str
    email_verified: bool
    account_id: int
    oms_id: int
    use_2fa: bool
