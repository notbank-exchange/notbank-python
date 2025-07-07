from dataclasses import dataclass


@dataclass
class DeleteBankAccountRequest:
    bank_account_id: str
