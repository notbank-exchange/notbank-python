import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import GetInstrumentRequest
from tests import test_helper


class TestGetInstrument(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(print)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_instrument(self):
        response = self.client.get_instrument(GetInstrumentRequest(
            instrument_id=1,
        ))
        print(response)
        



if __name__ == "__main__":
    unittest.main()
