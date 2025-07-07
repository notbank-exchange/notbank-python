import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.client_connection_factory import new_rest_client_connection
from notbank_python_sdk.requests_models.get_banks_request import GetBanksRequest
from tests import test_helper


class TestGetBanks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_ticker_success(self):
        response = self.client.get_banks(GetBanksRequest("CL"))
        print(response)


if __name__ == "__main__":
    unittest.main()
