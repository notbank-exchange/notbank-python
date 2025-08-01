import unittest
from uuid import UUID
from notbank_python_sdk.requests_models.delete_client_bank_account_request import DeleteClientBankAccountRequest
from notbank_python_sdk.requests_models.get_account_info_request import GetAccountInfoRequest

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.get_banks_request import GetBanksRequest


class TestDeleteClientBankAccounts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_delete_client_bank_account(self):
        response = self.client.delete_client_bank_account(
            DeleteClientBankAccountRequest(UUID('b49940d1-abf8-452a-a8a4-ece70bf53412')))
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
