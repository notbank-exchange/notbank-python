import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import GetTickerHistoryRequest
from tests import test_helper


class TestGetTickerHistory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_valid_instrument_id(self):
        response = self.client.get_ticker_history(GetTickerHistoryRequest(
            instrument_id=1,
            interval=60,
            from_date="2023-01-18 01:02:03",
            to_date="2023-08-31 23:59:59",
        ))



if __name__ == "__main__":
    unittest.main()
