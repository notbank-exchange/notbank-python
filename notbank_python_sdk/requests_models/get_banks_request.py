from dataclasses import dataclass


@dataclass
class GetBanksRequest:
    country: str
