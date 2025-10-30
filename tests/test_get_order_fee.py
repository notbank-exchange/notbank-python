from decimal import Decimal
import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import GetOrderFeeRequest
from notbank_python_sdk.constants import MakerTaker, OrderType, Side
from tests import test_helper


class TestGetOrderFee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_order_fee(self):
        response = self.client.get_order_fee(GetOrderFeeRequest(
            account_id=9,
            instrument_id=1,
            quantity=Decimal(0.5),
            price=Decimal(10000.0),
            order_type=OrderType.LIMIT,
            maker_taker=MakerTaker.MAKER,
            side=Side.BUY,
        ))


if __name__ == "__main__":
    unittest.main()
