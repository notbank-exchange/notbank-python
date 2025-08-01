from decimal import Decimal
import unittest
from uuid import UUID
from notbank_python_sdk.requests_models.create_fiat_deposit_request import CreateFiatDepositRequest
from notbank_python_sdk.requests_models.get_account_info_request import GetAccountInfoRequest

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.get_banks_request import GetBanksRequest


class TestCreateFiatDeposit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_create_fiat_deposit(self):
        response = self.client.create_fiat_deposit(CreateFiatDepositRequest(
            account_id=self.credentials.account_id,
            payment_method=1,
            currency="CLP",
            amount=Decimal("10"),
            bank_account_id=UUID("4172acac-f18e-41e2-8423-94e1c7feeebf")
        ))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
