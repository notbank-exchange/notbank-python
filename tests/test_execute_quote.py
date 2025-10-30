import unittest
from uuid import UUID

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import ExecuteQuoteRequest

from tests import test_helper


class TestCreateInverseQuote(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def create_inverse_quote(self):
        response = self.client.execute_quote(ExecuteQuoteRequest(
            UUID("c1c56ca3-75c3-4bb6-97e3-702448382cd3")))


if __name__ == "__main__":
    unittest.main()
