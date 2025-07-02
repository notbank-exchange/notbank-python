# models/get_enums.py
from typing import List
from dataclasses import dataclass, field


@dataclass
class EnumItem:
    name: str
    description: str
    number: int


@dataclass
class EnumsResponse:
    class_name: str
    property_name: str
    enums: List[EnumItem] = field(default_factory=list)

    @classmethod
    def from_dict(cls, d):
        return cls(
            class_name=d.get("Class"),
            property_name=d.get("Property"),
            enums=[EnumItem(**e) for e in d.get("Enums", [])]
        )
