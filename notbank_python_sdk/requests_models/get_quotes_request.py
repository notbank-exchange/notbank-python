from dataclasses import dataclass

from notbank_python_sdk.constants import QuoteMode


@dataclass
class GetQuotesRequest:
    mode: QuoteMode
