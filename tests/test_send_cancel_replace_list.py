from decimal import Decimal
import unittest
from notbank_python_sdk.constants import OrderType, Side, TimeInForce
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import CancelReplaceOrderRequest

from tests import test_helper


class TestSendCancelReplaceList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_send_cancel_replace_list_success(self):
        self.client.send_cancel_replace_list([
            CancelReplaceOrderRequest(
                order_id_to_replace=6696,
                order_type=OrderType.LIMIT,
                side=Side.BUY,
                account_id=7,
                instrument_id=1,
                quantity=Decimal("0.003"),
                time_in_force=TimeInForce.GTC,
            ),
            CancelReplaceOrderRequest(
                order_id_to_replace=6698,
                order_type=OrderType.LIMIT,
                side=Side.BUY,
                account_id=7,
                instrument_id=1,
                quantity=Decimal("0.004"),
                time_in_force=TimeInForce.GTC,
            ),
        ])


if __name__ == "__main__":
    unittest.main()
