import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import GetOpenOrdersRequest
from tests import test_helper


class TestGetOpenOrders(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_open_orders_success(self):
        response = self.client.get_open_orders(GetOpenOrdersRequest(
            account_id=9,
            instrument_id=1
        ))

if __name__ == "__main__":
    unittest.main()
