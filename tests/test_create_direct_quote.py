from decimal import Decimal
import unittest

from notbank_python_sdk.constants import QuoteOperation
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import CreateDirectQuoteRequest

from tests import test_helper


class TestCreateDirectQuote(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def create_direct_quote(self):
        response = self.client.create_direct_quote(CreateDirectQuoteRequest(
            account_id=123,
            from_currency="CLP",
            to_currency="BTC",
            from_amount=Decimal("100000"),
            operation=QuoteOperation.BUY,
        ))


if __name__ == "__main__":
    unittest.main()
