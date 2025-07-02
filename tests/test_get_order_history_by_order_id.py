import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_order_history_by_order_id import GetOrderHistoryByOrderIdRequest
from tests import test_helper


class TestGetOrderHistoryByOrderId(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_order_history_by_order_id_success(self):
        """Prueba exitosa: order_id válido."""
        request = GetOrderHistoryByOrderIdRequest(
            order_id=6459,
        )
        response = self.client.get_order_history_by_order_id(request)

        # Verificar que devuelve correctamente 1 estado de orden
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].order_id, 6459)
        self.assertEqual(response[0].account_name, "sample_user")
        self.assertEqual(response[0].order_state, "FullyExecuted")
        self.assertEqual(response[0].quantity_executed, 18307.63)

    def test_get_order_history_by_order_id_not_found(self):
        """Prueba: order_id inválido, no se encuentra el registro."""
        request = GetOrderHistoryByOrderIdRequest(
            order_id=999,
        )
        response = self.client.get_order_history_by_order_id(request)

        # Verificar que no se devuelven estados de orden
        self.assertEqual(len(response), 0)


# Punto de entrada para ejecutar pruebas
if __name__ == "__main__":
    unittest.main()
