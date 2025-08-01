

import unittest
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.get_whitelisted_addresses_request import GetWhitelistedAddressesRequest
from tests import test_helper


class TestCreateDepositAddress(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_create_deposit_address(self):
        response = self.client.get_whitelisted_addresses(
            GetWhitelistedAddressesRequest(self.credentials.account_id))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
