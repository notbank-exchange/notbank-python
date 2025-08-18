

import unittest
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.add_whitelisted_address_request import AddWhitelistedAddressRequest
from notbank_python_sdk.requests_models.get_whitelisted_addresses_request import GetWhitelistedAddressesRequest
from tests import test_helper


class TestAddWhiteListedAddresses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_add_whitelisted_addresses(self):
        response = self.client.add_whitelisted_addresses(
            AddWhitelistedAddressRequest(
                self.credentials.account_id,
                currency="BTC",
                network="BTC_TEST",
                address="tb1qrekfjtdrffe7r62fr4hspgka8qmzq0t3wu9z87",
                label="a label",
                otp="047973"))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
