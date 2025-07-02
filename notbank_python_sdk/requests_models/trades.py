from dataclasses import dataclass


@dataclass
class TradesRequest:
    market_pair: str
