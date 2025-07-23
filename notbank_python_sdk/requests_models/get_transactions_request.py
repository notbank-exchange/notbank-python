from dataclasses import dataclass


@dataclass
class GetTransactionsRequest:
    from_date: str
    to_date: str
    sort: str
    currency: str
    page: int
    page_size: int
