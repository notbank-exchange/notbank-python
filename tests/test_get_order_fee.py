from decimal import Decimal
import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_order_fee_request import GetOrderFeeRequest
from tests import test_helper


class TestGetOrderFee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_order_fee_success(self):
        """
        Prueba exitosa: Solicitud válida, devuelve la estimación de la comisión.
        """
        request = GetOrderFeeRequest(
            account_id=9,
            instrument_id=1,
            quantity=Decimal(0.5),
            price=Decimal(10000.0),
            order_type=2,
            maker_taker=1,
            side=0,
        )
        response = self.client.get_order_fee(request)

        # Verificaciones
        self.assertIsNotNone(response)
        self.assertEqual(response.order_fee, 0.00001)
        self.assertEqual(response.product_id, 2)

    def test_get_order_fee_not_found(self):
        """
        Prueba: Solicitud inválida, no se encuentra la estimación.
        """
        request = GetOrderFeeRequest(
            account_id=999,  # account_id inválido
            instrument_id=1,
            quantity=Decimal(0.5),
            price=Decimal(10000.0),
            order_type=2,
            maker_taker=1,
            side=0,
        )
        response = self.client.get_order_fee(request)

        # Verificaciones
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
