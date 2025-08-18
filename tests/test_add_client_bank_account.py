import unittest
from notbank_python_sdk.requests_models.add_client_bank_account_request import AddClientBankAccountRequest, BankAccountKind

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient


class TestAddClientBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_add_client_bank_account(self):
        response = self.client.add_client_bank_account(AddClientBankAccountRequest(
            country="CL",
            bank="11",
            number="123123",
            kind=BankAccountKind.AHORRO,
        ))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
