from dataclasses import dataclass
from uuid import UUID


@dataclass
class ExecuteQuoteRequest:
    request_id: UUID
