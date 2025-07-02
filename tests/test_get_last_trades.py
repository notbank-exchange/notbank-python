import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_last_trades import GetLastTradesRequest
from tests import test_helper


class TestGetLastTrades(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_valid_instrument_id(self):
        """
        Prueba: Obtener los últimos trades para un instrument_id válido.
        """
        request = GetLastTradesRequest(
            instrument_id=1,
            count=10,
        )
        response = self.client.get_last_trades(request)

        # Validaciones
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0].trade_id, 14)
        self.assertEqual(response[0].quantity, 0.02)
        self.assertEqual(response[0].price, 1970.0)
        self.assertEqual(response[0].direction, 1)  # UpTick

    def test_empty_response(self):
        """
        Prueba: Obtener trades para un instrument_id sin registros.
        """
        request = GetLastTradesRequest(
            instrument_id=999,
        )
        response = self.client.get_last_trades(request)

        # Validaciones
        self.assertEqual(len(response), 0)

    def test_invalid_instrument_id(self):
        """
        Prueba: Obtener trades para un instrument_id inválido.
        """
        request = GetLastTradesRequest(
            instrument_id=0,
        )

        with self.assertRaises(Exception) as context:
            self.client.get_last_trades(request)

        # Validación del mensaje de error
        self.assertEqual(str(context.exception), "Invalid instrument_id")


if __name__ == "__main__":
    unittest.main()
