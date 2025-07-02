import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_instruments_request import GetInstrumentsRequest
from tests import test_helper


class TestGetInstruments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_instruments_success(self):
        request = GetInstrumentsRequest(instrument_state="Both")
        response = self.client.get_instruments(request)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0].symbol, "ETHUSD")
        self.assertEqual(response[0].product1_symbol, "ETH")
        self.assertEqual(response[1].symbol, "TBTCUSD")
        self.assertEqual(response[1].product1_symbol, "TBTC")

    def test_get_instruments_failure(self):
        request = GetInstrumentsRequest()
        response = self.client.get_instruments(request)
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
