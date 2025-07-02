import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from tests import test_helper

class TestTicker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)


    def test_get_ticker_success(self):
        response = self.client.get_ticker()
        self.assertIsInstance(response, dict)
        self.assertEqual(len(response), 2)
        self.assertEqual(response['BTC_USD'].base_id, 1)
        self.assertEqual(response['BTC_USD'].last_price, 29000)
        self.assertEqual(response['ETH_USD'].base_id, 1027)
        self.assertEqual(response['ETH_USD'].last_price, 1970)

if __name__ == "__main__":
    unittest.main()
