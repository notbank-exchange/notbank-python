import unittest

from notbank_python_sdk.requests_models.cancel_order_request import CancelOrderRequest
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
        request = CancelOrderRequest(
            account_id=self.credentials.account_id,
            order_id=6500
        )
        try:
            response = self.client.cancel_order(request)
        except Exception as e:
            self.fail(f"Cancel order failed with exception: {e}")

    def test_cancel_order_success_cl_order_id(self):
        request = CancelOrderRequest(
            account_id=self.credentials.account_id,
            cl_order_id=777
        )
        try:
            response = self.client.cancel_order(request)
        except Exception as e:
            self.fail(f"Cancel order failed with exception: {e}")

    def test_cancel_order_not_authorized(self):
        request = CancelOrderRequest(
            account_id=self.credentials.account_id+123,
            cl_order_id=9999
        )
        try:
            self.client.cancel_order(request)
            self.fail("Expected NotbankException but none was raised")
        except Exception as e:
            pass


if __name__ == "__main__":
    unittest.main()
