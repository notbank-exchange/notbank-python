import unittest
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.get_level1_summary_min import GetLevel1SummaryMinRequest
from tests import test_helper


class TestGetLevel1SummaryMin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_valid_oms_id_and_instrument_ids(self):
        """
        Prueba: Obtener el resumen de nivel 1 mínimo para un OMSId y InstrumentIds válidos.
        """
        request = GetLevel1SummaryMinRequest(
            instrument_ids="[1]",
        )
        response = self.client.get_level1_summary_min(request)

        # Validaciones
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].instrument_id, 1)
        self.assertEqual(response[0].last_traded_px, 29900.0)
        self.assertEqual(response[0].rolling_24hr_volume, 0.0021)

    def test_empty_response(self):
        """
        Prueba: Obtener resumen de nivel 1 mínimo para un OMSId sin registros.
        """
        request = GetLevel1SummaryMinRequest()
        response = self.client.get_level1_summary_min(request)

        # Validaciones
        self.assertEqual(len(response), 0)

    def test_invalid_oms_id(self):
        """
        Prueba: Obtener resumen de nivel 1 mínimo para un OMSId inválido.
        """
        request = GetLevel1SummaryMinRequest()

        with self.assertRaises(Exception) as context:
            self.client.get_level1_summary_min(request)

        # Validación del mensaje de error
        self.assertEqual(str(context.exception), "Invalid OMSId")


if __name__ == "__main__":
    unittest.main()
