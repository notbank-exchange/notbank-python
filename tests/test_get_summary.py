import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from tests import test_helper


class TestInstrumentSummary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_summary_success(self):
        response = self.client.get_summary()
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0].trading_pairs, "BTC_USD")
        self.assertEqual(response[0].last_price, 29000)
        self.assertEqual(response[1].trading_pairs, "ETH_USD")
        self.assertEqual(response[1].last_price, 1970)


if __name__ == "__main__":
    unittest.main()
