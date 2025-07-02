import secrets
from hmac import HMAC
from hashlib import sha256

from notbank_python_sdk.requests_models.authenticate_request import AuthenticateRequestData, AuthenticateRequest


class Authenticator:
    @staticmethod
    def _new_nonce() -> str:
        return str(secrets.randbelow(10_000_000_00))

    @staticmethod
    def _get_request_signature(authenticate_request: AuthenticateRequest, nonce: str) -> str:
        message = nonce+str(authenticate_request.user_id) + \
            authenticate_request.api_public_key
        return HMAC(key=authenticate_request.api_secret_key.encode(),
                    msg=message.encode(),
                    digestmod=sha256).hexdigest()

    @classmethod
    def convert_data(cls, authenticate_request: AuthenticateRequest) -> AuthenticateRequestData:
        nonce = cls._new_nonce()
        signature = cls._get_request_signature(authenticate_request, nonce)
        return AuthenticateRequestData(
            api_key=authenticate_request.api_public_key,
            signature=signature,
            user_id=str(authenticate_request.user_id),
            nonce=nonce
        )
