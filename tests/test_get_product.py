from decimal import Decimal
import unittest
from notbank_python_sdk.error import NotbankException

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_product_request import GetProductRequest
from tests import test_helper


class TestGetProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.client = NotbankClient(connection)

    def test_get_product_success(self):
        response = self.client.get_product(GetProductRequest(product_id=1))
        print(response)


if __name__ == "__main__":
    unittest.main()
