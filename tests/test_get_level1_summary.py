import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_level1_summary import GetLevel1SummaryRequest
from tests import test_helper


class TestGetLevel1Summary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_valid_oms_id(self):
        """
        Prueba: Obtener el resumen de nivel 1 para un OMSId válido.
        """
        response = self.client.get_level1_summary()

        # Validaciones
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].instrument_id, 1)
        self.assertEqual(response[0].best_bid, 30000)
        self.assertEqual(response[0].last_traded_px, 29354.89)

    def test_empty_response(self):
        """
        Prueba: Obtener resumen de nivel 1 para un OMSId sin registros.
        """
        response = self.client.get_level1_summary()

        # Validaciones
        self.assertEqual(len(response), 0)

    def test_invalid_oms_id(self):
        """
        Prueba: Obtener resumen de nivel 1 para un OMSId inválido.
        """
        with self.assertRaises(Exception) as context:
            self.client.get_level1_summary()

        # Validación del mensaje de error
        self.assertEqual(str(context.exception), "Invalid OMSId")


if __name__ == "__main__":
    unittest.main()
