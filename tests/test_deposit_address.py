import unittest
from notbank_python_sdk.requests_models.create_bank_account_request import CreateBankAccountRequest
from notbank_python_sdk.requests_models.delete_bank_account_request import DeleteBankAccountRequest
from notbank_python_sdk.requests_models.get_bank_account_request import GetBankAccountRequest
from notbank_python_sdk.requests_models import *

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient


class TestGetBanks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_deposit_address(self):
        request = DepositAddressRequest(
            self.credentials.account_id, "USDT", "USDT_BSC_TEST")
        address = self.client.create_deposit_address(request)
        print(address)
        getted_addresses = self.client.get_deposit_addresses(request)
        print(getted_addresses)


if __name__ == "__main__":
    unittest.main()
