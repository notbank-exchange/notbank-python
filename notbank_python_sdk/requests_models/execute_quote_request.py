from dataclasses import dataclass
from uuid import UUID


@dataclass
class ExecuteQuoteRequest:
    quote_id: UUID
