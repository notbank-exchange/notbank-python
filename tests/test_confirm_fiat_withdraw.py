from uuid import UUID

import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import ConfirmFiatWithdrawRequest

from tests import test_helper


class TestGetBanks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_banks(self):
        response = self.client.confirm_fiat_withdraw(ConfirmFiatWithdrawRequest(
          withdrawal_id=UUID("32347216-4a4c-49ee-b0a5-1ad993fe522b"),
          attempt_code="123456",
        ))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
