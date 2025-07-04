import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.verification_level_config_request import VerificationLevelConfigRequest
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
        request = VerificationLevelConfigRequest(
            account_id=7,
        )
        response = self.client.get_instrument_verification_level_config(
            request)

        # Verificaciones
        self.assertIsNotNone(response)
        self.assertEqual(response.level, 1)
        self.assertEqual(len(response.instruments), 2)
        self.assertEqual(response.instruments[0].instrument_name, "BTCUSD")
        self.assertEqual(response.instruments[1].instrument_name, "ETHUSD")

    def test_get_instrument_verification_level_config_not_found(self):
        """
        Prueba: Solicitud inválida, no se encuentra la configuración.
        """
        request = VerificationLevelConfigRequest(
            account_id=999,  # account_id inválido
        )
        response = self.client.get_instrument_verification_level_config(
            request)

        # Verificaciones
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
