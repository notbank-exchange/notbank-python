import unittest

from notbank_python_sdk.requests_models import CancelOrderRequest
from notbank_python_sdk.notbank_client import NotbankClient
from tests import test_helper


class TestCancelOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_cancel_order_success_order_id(self):
        response = self.client.cancel_order(CancelOrderRequest(
            account_id=self.credentials.account_id,
            order_id=6500
        ))


if __name__ == "__main__":
    unittest.main()
