from dataclasses import dataclass

from notbank_python_sdk.websocket.message_type import MessageType


@dataclass
class MessageFrame:
    m: MessageType
    i: int
    n: str
    o: str
