import unittest
from uuid import UUID
from notbank_python_sdk.requests_models.confirm_whitelisted_address_request import ConfirmWhiteListedAddressRequest
from notbank_python_sdk.requests_models.delete_whitelisted_address_request import DeleteWhiteListedAddressRequest

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient


class TestDeleteWhitelistedAddress(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_delete_whitelisted_address(self):
        response = self.client.delete_whitelisted_address(DeleteWhiteListedAddressRequest(
            whitelisted_address_id=UUID(
                "3b84035d-c015-4646-bdee-bc0f500402cc"),
            account_id=self.credentials.account_id,
            otp="125814"))
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
