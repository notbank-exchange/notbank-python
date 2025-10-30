from decimal import Decimal
import unittest
from notbank_python_sdk.constants import OrderType, PegPriceType, Side, TimeInForce

from notbank_python_sdk.requests_models import CancelReplaceOrderRequest
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
        response = self.client.cancel_replace_order(CancelReplaceOrderRequest(
            order_id_to_replace=123456,
            client_order_id=0,
            order_type=OrderType.LIMIT,
            side=Side.BUY,
            account_id=20,
            instrument_id=9,
            limit_price=Decimal("1.363"),
            order_id_oco=123,
            time_in_force=TimeInForce.FOK,
            peg_price_type=PegPriceType.ASK,
            use_display_quantity=False,
            quantity=Decimal("7322.24"),
        ))


if __name__ == "__main__":
    unittest.main()
