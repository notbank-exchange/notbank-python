from decimal import Decimal
import unittest
from notbank_python_sdk.requests_models.create_crypto_withdraw_request import CreateCryptoWithdrawRequest
from notbank_python_sdk.requests_models.get_account_info_request import GetAccountInfoRequest

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.get_banks_request import GetBanksRequest


class TestGetBanks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()        
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_banks(self):
        response = self.client.create_crypto_withdraw(CreateCryptoWithdrawRequest(
          account_id=self.credentials.account_id,
          currency="BTC",
          network="BTC_TEST",
          address="tb1qrekfjtdrffe7r62fr4hspgka8qmzq0t3wu9z87",
          amount=Decimal("0.001"),
          otp="994618"
        ))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
