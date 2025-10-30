
import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import GetNetworksTemplatesRequest

from tests import test_helper


class TestGetNetworksTemplates(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            peek_message_out=test_helper.print_message_out, peek_message_in=test_helper.print_message_in)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_networks_templates(self):
        response = self.client.get_networks_templates(
            GetNetworksTemplatesRequest(currency="BTC"))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
