from decimal import Decimal
from uuid import UUID

import unittest

from notbank_python_sdk.constants import DepositPaymentMethod
from notbank_python_sdk.requests_models import CreateFiatWithdrawRequest
from notbank_python_sdk.notbank_client import NotbankClient

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
        response = self.client.create_fiat_withdraw(CreateFiatWithdrawRequest(
            account_id=self.credentials.account_id,
            payment_method=DepositPaymentMethod.BANK_TRANSFER,
            currency="CLP",
            amount=Decimal("1000"),
            bank_account_id=UUID("43438b99-70a4-4d98-8471-71f5a52b978b"),
        ))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
