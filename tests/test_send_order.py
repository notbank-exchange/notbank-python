from decimal import Decimal
import random
import unittest
from notbank_python_sdk.models.account_positions import AccountPosition
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.models.send_order import  SendOrderStatus
from notbank_python_sdk.requests_models.get_account_positions_request import GetAccountPositionsRequest
from notbank_python_sdk.requests_models.order_book import OrderBookRequest
from notbank_python_sdk.requests_models.send_order import OrderType, SendOrderRequest, Side, TimeInForce
from tests import test_helper


class TestSendOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_send_order_success(self):
        instrument = self.client.get_instrument_by_symbol("BTCUSDT")
        order_price = self._get_order_price()
        order_quantity = self._get_order_quantity()
        request = SendOrderRequest(
            instrument=instrument,
            account_id=self.credentials.account_id,
            time_in_force=TimeInForce.GTD,
            side=Side.Sell,
            quantity=order_quantity,
            limit_price=order_price,
            order_type=OrderType.Limit,
        )
        response = self.client.send_order(request)
        if response.status == SendOrderStatus.REJECTED:
            # order was rejected
            pass
        else:
            # order was accepted
            order_id = response.order_id

    def _get_order_price(self) -> Decimal:
        orderbook = self.client.get_order_book(
            OrderBookRequest("BTCUSDT", 1, 1))
        top_orderbook = orderbook.asks[0]
        delta = Decimal(random.randrange(10, 100))/1000
        order_price = top_orderbook.price + delta
        return order_price

    def _get_order_quantity(self) -> Decimal:
        ust_balance = self._get_balance("USDT")
        total_balance = ust_balance.amount
        return total_balance - \
            Decimal(random.random()) * (-(total_balance/2))

    def _get_balance(self, product_symbol: str) -> AccountPosition:
        positions = self.client.get_account_positions(
            GetAccountPositionsRequest(self.credentials.account_id))
        for position in positions:
            if position.product_symbol == product_symbol:
                return position
        raise Exception("no balance for product: " + product_symbol)

    def test_send_order_not_enough_funds(self):
        instrument = self.client.get_instrument_by_symbol("BTCUSDT")
        request = SendOrderRequest(
            instrument=instrument,
            account_id=self.credentials.account_id,
            time_in_force=TimeInForce.FOK,
            side=Side.Sell,
            quantity=Decimal("12"),
            order_type=OrderType.Market,
        )
        response = self.client.send_order(request)
        self.assertEqual(response.status, "Rejected")
        self.assertEqual(response.errormsg, "Not_Enough_Funds")


if __name__ == "__main__":
    unittest.main()
