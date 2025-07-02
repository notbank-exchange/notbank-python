import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_instrument_request import GetInstrumentRequest
from tests import test_helper


class TestGetInstrument(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_instrument_success(self):
        """
        Prueba exitosa: oms_id e instrument_id válidos, devuelve los detalles del instrumento.
        """
        request = GetInstrumentRequest(
            instrument_id=1,
        )
        response = self.client.get_instrument(request)

        # Verificaciones
        self.assertIsNotNone(response)
        self.assertEqual(response.symbol, "BTCUSD")
        self.assertEqual(response.product1_symbol, "BTC")
        self.assertEqual(response.session_status, "Running")
        self.assertEqual(response.minimum_quantity, 0.001)
        self.assertEqual(response.minimum_price, 10.0)

    def test_get_instrument_not_found(self):
        """
        Prueba: Instrumento no encontrado, devuelve None.
        """
        request = GetInstrumentRequest(
            instrument_id=999,  # instrument_id inválido
        )
        response = self.client.get_instrument(request)

        # Verificaciones
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
