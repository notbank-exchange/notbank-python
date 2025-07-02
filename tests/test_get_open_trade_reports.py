import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_open_trade_reports import GetOpenTradeReportsRequest
from tests import test_helper


class TestGetOpenTradeReports(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)


    def test_get_open_trade_reports_success(self):
        request = GetOpenTradeReportsRequest(
            account_id=9,
        )
        response = self.client.get_open_trade_reports(request)

        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].order_id, 6723)
        self.assertEqual(response[0].price, 29500.0)
        self.assertEqual(response[0].quantity, 0.2563)
        self.assertEqual(response[0].order_state, "Working")
        self.assertEqual(response[0].avg_price, 0.0)

    def test_get_open_trade_reports_not_found(self):
        request = GetOpenTradeReportsRequest(
            account_id=999,
        )
        response = self.client.get_open_trade_reports(request)
        self.assertEqual(len(response), 0)

    def test_invalid_oms_id(self):
        request = GetOpenTradeReportsRequest(
            account_id=9,
        )

        with self.assertRaises(Exception) as context:
            self.client.get_open_trade_reports(request)
        self.assertIn("Invalid OMSId", str(context.exception))


if __name__ == "__main__":
    unittest.main()
