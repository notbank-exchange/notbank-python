from dataclasses import dataclass


@dataclass
class UserInfo:
    user_id: int
    user_name: str
    email: str
    password_hash: str
    pending_email_code: str
    email_verified: bool
    account_id: int
    date_time_created: str
    affiliate_id: int
    referer_id: int
    oms_id: int
    use_2fa: bool
    salt: str
    pending_code_time: str
    locked: bool
    locked_time: str
    number_of_failed_attempt: int
    margin_borrower_enabled: bool
    margin_acquisition_halt: bool
    operator_id: int
