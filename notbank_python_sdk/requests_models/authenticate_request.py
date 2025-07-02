from dataclasses import dataclass
from typing import Union


@dataclass
class AuthenticateRequest:
    api_public_key: str
    api_secret_key: str
    user_id: Union[str, int]


@dataclass
class AuthenticateRequestData:
    api_key: str
    signature: str
    user_id: str
    nonce: str
