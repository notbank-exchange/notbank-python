import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_last_trades import GetLastTradesRequest
from tests import test_helper


class TestGetLastTrades(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_valid_instrument_id(self):
        response = self.client.get_last_trades(GetLastTradesRequest(
            instrument_id=1,
            count=10,
        ))


if __name__ == "__main__":
    unittest.main()
