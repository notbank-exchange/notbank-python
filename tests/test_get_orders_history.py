import unittest

from notbank_python_sdk.notbank_client import NotbankClient


from notbank_python_sdk.requests_models.get_orders_history import GetOrdersHistoryRequest
from tests import test_helper


class TestGetOrdersHistory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_orders_history_success(self):
        """Prueba exitosa: Devuelve el historial de órdenes válido."""
        request = GetOrdersHistoryRequest(
            account_id=1,
        )
        response = self.client.get_orders_history(request)

        # Verifica que devuelve correctamente 1 orden
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].order_id, 6713)
        self.assertEqual(response[0].order_state, "FullyExecuted")
        self.assertEqual(response[0].orig_quantity, 0.01)
        self.assertEqual(response[0].avg_price, 6000.0)

    def test_get_orders_history_empty(self):
        """Prueba sin datos: Devuelve una lista vacía."""
        request = GetOrdersHistoryRequest(
            account_id=999,
        )
        response = self.client.get_orders_history(request)

        # Verifica que no se devuelven órdenes
        self.assertEqual(len(response), 0)


# Punto de entrada para ejecutar pruebas
if __name__ == "__main__":
    unittest.main()
