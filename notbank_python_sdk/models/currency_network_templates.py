from dataclasses import dataclass
from typing import List

from notbank_python_sdk.models.network_template import NetworkTemplate


@dataclass
class CurrencyNetworkTemplates:
    currency: str
    network: str
    network_name: str
    network_protocol: str
    template: List[NetworkTemplate]
