from typing import Callable
from dataclasses import dataclass
from typing import Callable

from notbank_python_sdk.error import NotbankException


@dataclass
class Callback:
    id: str
    builder: Callable[[
        Callable[[NotbankException], None]],
        Callable[[str], None]]
