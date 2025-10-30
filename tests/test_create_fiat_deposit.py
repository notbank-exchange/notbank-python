from decimal import Decimal
import unittest
from uuid import UUID
from notbank_python_sdk.constants import DepositPaymentMethod
from notbank_python_sdk.requests_models import CreateFiatDepositRequest


from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient


class TestCreateFiatDeposit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_create_fiat_deposit(self):
        self.client.create_fiat_deposit(CreateFiatDepositRequest(
            account_id=self.credentials.account_id,
            payment_method=DepositPaymentMethod.BANK_TRANSFER,
            currency="ARS",
            amount=Decimal("10"),
            bank_account_id=UUID("4d677d9c-81e1-45d2-9903-43fd599b6599")
        ))


if __name__ == "__main__":
    unittest.main()
