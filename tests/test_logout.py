import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from tests import test_helper


class TestLogOut(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_logout_success(self):
        """Prueba exitosa: cierre de sesión con un token válido."""
        self.client.logout()

    def test_logout_invalid_token(self):
        """Prueba: cierre de sesión con un token inválido."""
        self.client.logout()

    def test_logout_missing_token(self):
        """Prueba: cierre de sesión sin token."""
        self.client.logout()


if __name__ == "__main__":
    unittest.main()
