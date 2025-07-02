import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_account_positions_request import GetAccountPositionsRequest
from tests import test_helper


class TestGetAccountPositions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_account_positions_success(self):
        request = GetAccountPositionsRequest(
            account_id=self.credentials.account_id)
        account_positions = self.client.get_account_positions(request)
            

# Punto de entrada para ejecutar pruebas
if __name__ == "__main__":
    unittest.main()
