from decimal import Decimal
import unittest
from notbank_python_sdk.error import NotbankException
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.cancel_replace_order_request import CancelReplaceOrderRequest

from tests import test_helper


class TestSendCancelReplaceList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_send_cancel_replace_list_success(self):
        """Prueba exitosa, devuelve 'True'."""
        request = [
            CancelReplaceOrderRequest(
                order_id_to_replace=6696,
                order_type="Limit",
                side=0,  # Buy
                account_id=7,
                instrument_id=1,
                quantity=Decimal("0.003"),
                time_in_force=1,  # GTC
            ),
            CancelReplaceOrderRequest(
                order_id_to_replace=6698,
                order_type="Limit",
                side=0,  # Buy
                account_id=7,
                instrument_id=1,
                quantity=Decimal("0.004"),
                time_in_force=1,  # GTC
            ),
        ]

        self.client.send_cancel_replace_list(request)

    def test_send_cancel_replace_list_invalid_request(self):
        """Prueba fallida: falta un campo obligatorio, devuelve 'False'."""
        # Crear el objeto con todos los campos
        invalid_order = CancelReplaceOrderRequest(
            order_id_to_replace=6696,
            order_type="Limit",
            side=0,  # Buy
            account_id=7,
            instrument_id=1,
            quantity=Decimal("0.003"),  # Campo obligatorio
            time_in_force=1,  # GTC
        )

        # Eliminar el campo 'Quantity' después de la creación
        delattr(invalid_order, "quantity")

        try:
            self.client.send_cancel_replace_list(
                [invalid_order]
            )
        except NotbankException as e:
            self.assertEqual(str(e), "Invalid Request")
            self.assertEqual(e.code, 100)

    def test_send_cancel_replace_list_empty_list(self):
        """Prueba exitosa: lista vacía, devuelve 'False'."""
        request = []

        try:
            self.client.send_cancel_replace_list(request)
        except NotbankException as e:
            self.assertEqual(str(e), "Invalid Request")
            self.assertEqual(e.code, 100)


if __name__ == "__main__":
    unittest.main()
