from decimal import Decimal
import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import CreateInverseQuoteRequest

from tests import test_helper


class TestCreateInverseQuote(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def create_inverse_quote(self):
        response = self.client.create_inverse_quote(CreateInverseQuoteRequest(
            account_id=123,
            from_currency="CLP",
            to_currency="BTC",
            to_amount=Decimal("100000")
        ))


if __name__ == "__main__":
    unittest.main()
