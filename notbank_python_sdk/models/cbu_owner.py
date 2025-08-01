
from dataclasses import dataclass


@dataclass
class CbuOwner:
    person_type: str
    cuit: str
    name: str
