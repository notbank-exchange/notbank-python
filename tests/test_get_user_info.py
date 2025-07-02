
import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.models.user_info import UserInfo
from notbank_python_sdk.requests_models.get_user_info import GetUserInfoRequest
from tests import test_helper


class TestGetUserInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_user_info_response_ok(self):
        """
        Prueba exitosa: obtiene la información de usuario correcta según el mock.
        """
        req = GetUserInfoRequest(user_id=1)
        response = self.client.get_user_info(req)

        self.assertIsInstance(response, UserInfo)
        self.assertEqual(response.user_id, 1)
        self.assertEqual(response.user_name, "usuario_test")
        self.assertEqual(response.email, "test@email.com")
        self.assertEqual(response.account_id, 10)
        self.assertTrue(response.email_verified)
        self.assertFalse(response.locked)
        self.assertTrue(response.margin_borrower_enabled)


if __name__ == "__main__":
    unittest.main()
