import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_order_status import GetOrderStatusRequest
from tests import test_helper


class TestGetOrderStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_order_status_success(self):
        """
        Prueba exitosa: obtiene el estado de una orden válida.
        """
        request = GetOrderStatusRequest(
            account_id=7,
            order_id=6562,
        )
        response = self.client.get_order_status(request)

        # Verificamos que la respuesta contiene los datos esperados
        self.assertIsNotNone(response)
        self.assertEqual(response.order_id, 6562)
        self.assertEqual(response.side, "Buy")
        self.assertEqual(response.price, 23436.0)
        self.assertEqual(response.account_name, "sample_user")


if __name__ == "__main__":
    unittest.main()
