import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.user_accounts import GetUserAccountsRequest
from tests import test_helper


class TestGetUserAccounts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_user_accounts_single(self):
        request = GetUserAccountsRequest(user_id=1)
        response = self.client.get_user_accounts(request)
        self.assertIsInstance(response, list)

    def test_get_user_accounts_multiple(self):
        request = GetUserAccountsRequest(user_id=5)
        response = self.client.get_user_accounts(request)
        self.assertEqual(response, [7, 8, 9])

    def test_get_user_accounts_default_user(self):
        request = GetUserAccountsRequest()
        response = self.client.get_user_accounts(request)
        self.assertEqual(response, [6])

    def test_get_user_accounts_no_result(self):
        request = GetUserAccountsRequest(user_id=999)
        response = self.client.get_user_accounts(request)
        self.assertEqual(response, [])


if __name__ == "__main__":
    unittest.main()
