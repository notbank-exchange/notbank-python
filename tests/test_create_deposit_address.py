import unittest
from notbank_python_sdk.requests_models.deposit_address_request import DepositAddressRequest

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient


class TestCreateDepositAddress(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()        
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_create_deposit_address(self):
        response = self.client.create_deposit_address(DepositAddressRequest(self.credentials.account_id, "BTC","BTC_TEST"))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
