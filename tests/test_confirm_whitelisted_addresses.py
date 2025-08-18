import unittest
from uuid import UUID
from notbank_python_sdk.requests_models.confirm_whitelisted_address_request import ConfirmWhiteListedAddressRequest

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient


class TestCreateDepositAddress(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_create_deposit_address(self):
        response = self.client.confirm_whitelisted_address(ConfirmWhiteListedAddressRequest(
            whitelisted_address_id=UUID(
                "ab38462b-e6ec-435c-a67c-e4c3e29f5b72"),
            account_id=self.credentials.account_id,
            sms_code="0564225"))
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
