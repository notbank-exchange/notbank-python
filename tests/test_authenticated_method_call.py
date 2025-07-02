from unittest import TestCase, main

from notbank_python_sdk.error import NotbankException
from notbank_python_sdk.requests_models.account_fees_request import AccountFeesRequest
from notbank_python_sdk.requests_models.authenticate_request import AuthenticateRequest
from notbank_python_sdk.requests_models.get_account_trades import GetAccountTradesRequest
from notbank_python_sdk.notbank_client import NotbankClient
from tests.test_helper import load_credentials, new_websocket_client_connection, new_rest_client_connection


class AuthenticatedMethodTestCase(TestCase):
    def test_rest_authentication(self):
        rest_client_connection = new_rest_client_connection()
        system_client = NotbankClient(rest_client_connection)
        credentials = load_credentials('keys.json')
        auth_response = system_client.authenticate(AuthenticateRequest(
            api_public_key=credentials.public_key,
            api_secret_key=credentials.secret_key,
            user_id=credentials.user_id,
        ))
        try:
            fees = system_client.get_account_fees(AccountFeesRequest(9))
        except NotbankException as e:
            print(f"error: {e}")

    def test_websocket_authentication(self):
        websocket_client_connection = new_websocket_client_connection()
        websocket_client_connection.connect()
        system_client = NotbankClient(websocket_client_connection)
        credentials = load_credentials('keys.json')
        auth_response = system_client.authenticate(AuthenticateRequest(
            api_public_key=credentials.public_key,
            api_secret_key=credentials.secret_key,
            user_id=credentials.user_id,
        ))
        try:
            account_trades = system_client.get_account_trades(
                GetAccountTradesRequest(1, credentials.account_id))
        except NotbankException as e:
            print(f"error: {e}")
        websocket_client_connection.close()


if __name__ == '__main__':
    main()
