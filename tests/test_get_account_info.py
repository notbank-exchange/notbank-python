import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_account_info_request import GetAccountInfoRequest
from tests import test_helper


class TestGetAccountInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)


    def test_get_account_info_success(self):
        """Prueba exitosa: oms_id y account_id válidos."""
        request = GetAccountInfoRequest(account_id=7)
        response = self.client.get_account_info(request)
        self.assertEqual(response.account_name, "sample_user")
        self.assertEqual(response.account_type, "Asset")
        self.assertEqual(response.risk_type, "Normal")

    def test_get_account_info_default_account(self):
        """Prueba: account_id no definido, devuelve cuenta por defecto."""
        request = GetAccountInfoRequest()
        response = self.client.get_account_info(request)
        self.assertEqual(response.account_id, 1)
        self.assertEqual(response.account_name, "default_user")


if __name__ == "__main__":
    unittest.main()
