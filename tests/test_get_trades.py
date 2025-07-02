import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.trades import TradesRequest
from tests import test_helper


class TestTrades(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_trades_success(self):
        request = TradesRequest(
            market_pair="BTCUSD"
        )
        response = self.client.get_trades(request)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0].trade_id, 1)
        self.assertEqual(response[0].price, 29000)
        self.assertEqual(response[0].type, "buy")
        self.assertEqual(response[1].trade_id, 2)
        self.assertEqual(response[1].price, 28800)
        self.assertEqual(response[1].type, "sell")


if __name__ == "__main__":
    unittest.main()
