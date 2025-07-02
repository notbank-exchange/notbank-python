import unittest
from notbank_python_sdk.models.level1_ticker import Level1Ticker
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.level1 import GetLevel1Request
from tests import test_helper


class TestGetLevel1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_level1_success(self):
        request = GetLevel1Request(instrument_id=1)
        response = self.client.get_level1(request)
        self.assertIsInstance(response, Level1Ticker)
        self.assertEqual(response.oms_id, 1)
        self.assertEqual(response.best_bid, 28700)
        self.assertEqual(response.instrument_id, 1)
        self.assertEqual(response.last_traded_qty, 0.001)

    def test_get_level1_no_result(self):
        request = GetLevel1Request(instrument_id=2)
        response = self.client.get_level1(request)
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
