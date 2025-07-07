from dataclasses import dataclass


@dataclass
class GetBankAccountRequest:
    bank_account_id: str
