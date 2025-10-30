from decimal import Decimal
import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import GetInstrumentRequest

from notbank_python_sdk.requests_models import OrderType, PegPriceType, SendOrderRequest, Side, TimeInForce

from tests import test_helper


class TestSendOrderList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_valid_order_list(self):
        """Prueba válida: Lista de órdenes correcta."""
        instrument = self.client.get_instrument(GetInstrumentRequest(2))
        response = self.client.send_order_list([
            SendOrderRequest(
                instrument=instrument,
                account_id=185,
                time_in_force=TimeInForce.GTC,
                side=Side.SELL,
                quantity=Decimal("0.02"),
                order_type=OrderType.LIMIT,
                peg_price_type=PegPriceType.ASK,
                limit_price=Decimal(23436),
                use_display_quantity=False,
            ),
            SendOrderRequest(
                instrument=instrument,
                account_id=185,
                time_in_force=TimeInForce.GTC,
                side=Side.SELL,
                quantity=Decimal("0.05"),
                order_type=OrderType.LIMIT,
                peg_price_type=PegPriceType.ASK,
                limit_price=Decimal(23436),
                use_display_quantity=False,
            )
        ])

    def test_empty_order_list(self):
        """Prueba inválida: Lista de órdenes vacía."""
        request = []

        with self.assertRaises(Exception) as context:
            self.client.send_order_list(request)

        # Validaciones
        self.assertEqual(str(context.exception), "Empty order list")


if __name__ == "__main__":
    unittest.main()
