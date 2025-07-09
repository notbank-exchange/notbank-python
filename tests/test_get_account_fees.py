import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.account_fees_request import AccountFeesRequest

from tests import test_helper


class TestGetAccountInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)


    def test_get_account_fees(self):
        account_fees = self.client.get_account_fees(AccountFeesRequest(self.credentials.account_id))
        print(account_fees)


if __name__ == "__main__":
    unittest.main()
