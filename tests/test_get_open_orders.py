import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_open_orders import GetOpenOrdersRequest
from tests import test_helper


class TestGetOpenOrders(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_open_orders_success(self):
        request = GetOpenOrdersRequest(
            account_id=9,
            instrument_id=1
        )
        response = self.client.get_open_orders(request)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].order_id, 6598)
        self.assertEqual(response[0].quantity, 1.0)
        self.assertEqual(response[0].order_type, "StopMarket")

    def test_get_open_orders_no_results(self):
        request = GetOpenOrdersRequest(
            account_id=10
        )
        response = self.client.get_open_orders(request)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 0)


if __name__ == "__main__":
    unittest.main()
