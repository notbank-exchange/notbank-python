from decimal import Decimal
import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.modify_order import ModifyOrderRequest
from notbank_python_sdk.core.endpoints import Endpoints
from tests import test_helper


class TestModifyOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_modify_order_success(self):
        """Prueba exitosa: modificación de orden válida."""
        request = ModifyOrderRequest(
            order_id=6507,
            instrument_id=9,
            quantity=Decimal(0.1),
            account_id=9,
        )
        self.client.modify_order(request)

    def test_modify_order_invalid_quantity(self):
        """Prueba fallida: cantidad inválida (mayor que la cantidad actual)."""
        request = ModifyOrderRequest(
            order_id=6507,
            instrument_id=9,
            quantity=Decimal(1.5),  # Cantidad inválida
            account_id=9,
        )
        self.client.modify_order(request)

if __name__ == "__main__":
    unittest.main()
