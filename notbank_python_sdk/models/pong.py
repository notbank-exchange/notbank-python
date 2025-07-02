from dataclasses import dataclass
from enum import Enum


class PongType(str, Enum):
    PONG = "PONG"


@dataclass
class Pong:
    msg: PongType
