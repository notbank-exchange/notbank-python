import unittest
from unittest.mock import MagicMock
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.core.endpoints import WebSocketEndpoint
from notbank_python_sdk.models.web_authenticate_user_websocket import WebAuthenticateUserResponse
from notbank_python_sdk.requests_models.web_authenticate_user_request import WebAuthenticateUserRequest
from tests import test_helper


class TestWebAuthenticateUserIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_websocket_client_connection()
        cls.credentials = test_helper.load_credentials()
        connection.connect()
        cls.client = NotbankClient(connection)

    def test_initialization(self):
        response = self.client.web_authenticate_user(WebAuthenticateUserRequest(
            session_token="existingsessiontoken",

        ))


if __name__ == "__main__":
    unittest.main()
