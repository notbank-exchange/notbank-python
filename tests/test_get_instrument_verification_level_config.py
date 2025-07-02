import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_instrument_verification_level_config_request import GetVerificationLevelConfigRequest
from tests import test_helper


class TestGetInstrumentVerificationLevelConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_instrument_verification_level_config_success(self):
        """
        Prueba exitosa: Solicitud válida, devuelve la configuración de niveles de verificación.
        """
        request = GetVerificationLevelConfigRequest(
            account_id=7,
        )
        response = self.client.get_verification_level_config(
            request)

        # Verificaciones
        self.assertIsNotNone(response)
        self.assertEqual(response.level, 1)
        self.assertEqual(len(response.products), 2)
        self.assertEqual(response.products[0].product_name, "BTCUSD")
        self.assertEqual(response.products[1].product_name, "ETHUSD")

    def test_get_instrument_verification_level_config_not_found(self):
        """
        Prueba: Solicitud inválida, no se encuentra la configuración.
        """
        request = GetVerificationLevelConfigRequest(
            account_id=999,  # account_id inválido
        )
        response = self.client.get_verification_level_config(
            request)

        # Verificaciones
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
