import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_account_trades import GetAccountTradesRequest
from tests import test_helper


class TestGetAccountTrades(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_account_trades_success(self):
        request = GetAccountTradesRequest(
            account_id=7,
            start_index=0,
            depth=2
        )
        response = self.client.get_account_trades(request)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].trade_id, 916)
        self.assertEqual(response[0].account_name, "sample_user")
        self.assertEqual(response[0].quantity, 0.02)

    def test_get_account_trades_no_results(self):
        request = GetAccountTradesRequest(
            account_id=10
        )
        response = self.client.get_account_trades(request)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 0)


if __name__ == "__main__":
    unittest.main()
