import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_ticker_history import GetTickerHistoryRequest
from tests import test_helper


class TestGetTickerHistory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_valid_instrument_id(self):
        """
        Prueba: Obtener historial de ticker con un instrument_id válido.
        """
        request = GetTickerHistoryRequest(
            instrument_id=1,
            interval=60,
            from_date="2023-01-18 01:02:03",
            to_date="2023-08-31 23:59:59",
        )
        response = self.client.get_ticker_history(request)

        # Validaciones
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].instrument_id, 1)
        self.assertEqual(response[0].high, 28432.44)
        self.assertEqual(response[0].volume, 0.0)

    def test_empty_response(self):
        """
        Prueba: Obtener historial de ticker con un instrument_id que no tiene registros.
        """
        request = GetTickerHistoryRequest(
            instrument_id=999,
            interval=60,
            from_date="2023-01-18 01:02:03",
            to_date="2023-08-31 23:59:59",
        )
        response = self.client.get_ticker_history(request)

        # Validaciones
        self.assertEqual(len(response), 0)

    def test_invalid_instrument_id(self):
        """
        Prueba: Obtener historial de ticker con un instrument_id inválido.
        """
        request = GetTickerHistoryRequest(
            instrument_id=0,
            interval=60,
            from_date="2023-01-18 01:02:03",
            to_date="2023-08-31 23:59:59",
        )

        with self.assertRaises(Exception) as context:
            self.client.get_ticker_history(request)

        # Validación del mensaje de error
        self.assertEqual(str(context.exception), "Invalid instrument_id")


if __name__ == "__main__":
    unittest.main()
