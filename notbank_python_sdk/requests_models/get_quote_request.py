from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetQuoteRequest:
    quote_id: UUID
