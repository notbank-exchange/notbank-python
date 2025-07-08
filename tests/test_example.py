import unittest

from notbank_python_sdk.models.send_order import SendOrderStatus
from notbank_python_sdk.requests_models.get_account_positions_request import GetAccountPositionsRequest
from notbank_python_sdk.requests_models.order_book import OrderBookRequest
from notbank_python_sdk.requests_models.send_order import OrderType, SendOrderRequest, Side, TimeInForce
from tests import test_helper

from notbank_python_sdk.requests_models import *


class TestSendOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.credentials = test_helper.load_credentials()

    def test_send_order_success(self):
        from decimal import Decimal
        import random

        from notbank_python_sdk.notbank_client import NotbankClient
        from notbank_python_sdk.client_connection_factory import new_rest_client_connection

        account_id: int = 13  # must be user account id

        # instantiate client
        test_url = "stgapi.notbank.exchange"
        rest_connection = new_rest_client_connection(test_url)
        client = NotbankClient(rest_connection)

        # authentication (same for rest client or websocket client)
        authenticate = client.authenticate(
            AuthenticateRequest(
                api_public_key=self.credentials.public_key,
                api_secret_key=self.credentials.secret_key,
                user_id=self.credentials.user_id,
            )
        )
        if not authenticate.authenticated:
            raise Exception("client not authenticated")

        # get USDT user balance (also known as position)
        positions = client.get_account_positions(
            GetAccountPositionsRequest(account_id))
        usdt_balance = None
        product = "USDT"
        market_pair = "BTCUSDT"
        for position in positions:
            if position.product_symbol == product:
                usdt_balance = position
        if usdt_balance is None:
            raise Exception("user has no balance")

        # define order_amount (between all usdt_balance and half usdt_balance)
        total_balance = usdt_balance.amount
        quantity_to_spend = total_balance - \
            Decimal(random.random()) * (total_balance/2)

        # define order_price (around market top)
        orderbook = client.get_order_book(
            OrderBookRequest(market_pair, level=2, depth=5))
        top_orderbook = orderbook.bids[0]
        delta = Decimal(random.randrange(10, 100))/1000
        order_price = top_orderbook.price + delta

        order_quantity = quantity_to_spend / order_price

        # send order
        instrument = client.get_instrument_by_symbol(market_pair)
        request = SendOrderRequest(
            instrument=instrument,
            account_id=account_id,
            time_in_force=TimeInForce.GTC,
            side=Side.Buy,
            quantity=order_quantity,
            limit_price=order_price,
            order_type=OrderType.Limit,
        )
        response = client.send_order(request)
        # handle order result
        if response.status == SendOrderStatus.REJECTED:
            # order was rejected
            raise Exception("rejected order")
        else:
            # order was accepted
            order_id = response.order_id

        client.close()


if __name__ == "__main__":
    unittest.main()
