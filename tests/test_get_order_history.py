import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_order_history import GetOrderHistoryRequest
from tests import test_helper


class TestGetOrderHistory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_order_history_success(self):
        request = GetOrderHistoryRequest(
            account_id=7,
        )
        response = self.client.get_order_history(request)

        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].order_id, 6713)
        self.assertEqual(response[0].price, 0.0)
        self.assertEqual(response[0].quantity, 0.0)
        self.assertEqual(response[0].order_state, "FullyExecuted")
        self.assertEqual(response[0].avg_price, 6000.0)

    def test_get_order_history_not_found(self):
        request = GetOrderHistoryRequest(
            account_id=999,
        )
        response = self.client.get_order_history(request)
        self.assertEqual(len(response), 0)

    def test_invalid_oms_id(self):
        request = GetOrderHistoryRequest(
            account_id=7,
        )

        with self.assertRaises(Exception) as context:
            self.client.get_order_history(request)

        self.assertIn("Endpoint desconocido", str(context.exception))


if __name__ == "__main__":
    unittest.main()
