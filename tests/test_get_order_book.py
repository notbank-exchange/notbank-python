import unittest

from notbank_python_sdk.models.order_book import OrderBook
from notbank_python_sdk.requests_models.order_book import OrderBookRequest
from notbank_python_sdk.notbank_client import NotbankClient
from tests import test_helper
from tests.test_helper import new_websocket_client_connection


class TestOrderBook(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_websocket_client_connection()
        connection.connect()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    @classmethod
    def tearDownClass(cls):
        cls.client.close()

    def test_get_order_book(self):
        request = OrderBookRequest(
            market_pair="BTCUSD",
            level=-2,
            depth=10
        )
        orderbook = self.client.get_order_book(request)
        self.assertIsInstance(orderbook, OrderBook)


if __name__ == "__main__":
    unittest.main()
