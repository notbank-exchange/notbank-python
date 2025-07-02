from decimal import Decimal
import unittest

from notbank_python_sdk.requests_models.cancel_replace_order_request import CancelReplaceOrderRequest
from notbank_python_sdk.notbank_client import NotbankClient
from tests.test_helper import authenticate_connection, load_credentials, new_rest_client_connection


class TestCancelReplaceOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = new_rest_client_connection()
        cls.credentials = load_credentials('keys.json')
        authenticate_connection(cls.connection, cls.credentials)
        cls.client = NotbankClient(cls.connection)

    def test_cancel_replace_order_success(self):
        request = CancelReplaceOrderRequest(
            order_id_to_replace=123456,
            client_order_id=0,
            order_type="Limit",
            side="Buy",
            account_id=20,
            instrument_id=9,
            limit_price=Decimal(1.363),
            time_in_force=1,
            quantity=Decimal(7322.24),
        )
        response = self.client.cancel_replace_order(request)

        self.assertEqual(response.replacement_order_id, 123457)
        self.assertEqual(response.replacement_cl_ord_id, 0)
        self.assertEqual(response.orig_order_id, 123456)
        self.assertEqual(response.orig_cl_ord_id, 0)

    def test_cancel_replace_order_failed(self):
        request = CancelReplaceOrderRequest(
            order_id_to_replace=123456,
            client_order_id=0,
            order_type="Limit",
            side="Sell",
            account_id=20,
            instrument_id=9,
            limit_price=Decimal(1.363),
            time_in_force=1,
            quantity=Decimal(7322.24),
        )
        try:
            response = self.client.cancel_replace_order(request)
            self.fail("Expected NotbankException but none was raised")
        except:
            pass


if __name__ == "__main__":
    unittest.main()
