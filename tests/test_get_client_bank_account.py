import unittest
from uuid import UUID
from notbank_python_sdk.requests_models.get_account_info_request import GetAccountInfoRequest
from notbank_python_sdk.requests_models.get_client_bank_account_request import GetClientBankAccountRequest

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.get_banks_request import GetBanksRequest


class TestClientGetBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()        
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_client_get_bank_account(self):
        response = self.client.get_client_bank_account(GetClientBankAccountRequest(UUID('b49940d1-abf8-452a-a8a4-ece70bf53412')))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
