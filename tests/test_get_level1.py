import unittest
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import GetLevel1Request
from tests import test_helper


class TestGetLevel1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.client = NotbankClient(connection)

    def test_get_level1_success(self):
        response = self.client.get_level1(GetLevel1Request(instrument_id=1))


if __name__ == "__main__":
    unittest.main()
