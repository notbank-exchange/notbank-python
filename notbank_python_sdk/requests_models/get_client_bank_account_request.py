from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetClientBankAccountRequest:
    bank_account_id: UUID
