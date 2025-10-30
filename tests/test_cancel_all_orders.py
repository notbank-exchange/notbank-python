import unittest

from notbank_python_sdk.requests_models.cancel_all_orders import CancelAllOrdersRequest
from notbank_python_sdk.notbank_client import NotbankClient
from tests import test_helper


class TestCancelAllOrders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_cancel_all_orders_success(self):
        self.client.cancel_all_orders(CancelAllOrdersRequest(
            account_id=self.credentials.account_id,
            instrument_id=1,
        ))
        

if __name__ == "__main__":
    unittest.main()
