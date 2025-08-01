from dataclasses import dataclass
from uuid import UUID


@dataclass
class DeleteClientBankAccountRequest:
    bank_account_id: UUID
