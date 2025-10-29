import unittest
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import GetLevel1SummaryMinRequest
from tests import test_helper


class TestGetLevel1SummaryMin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(print, print)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_valid_oms_id_and_instrument_ids(self):
        response = self.client.get_level1_summary_min(GetLevel1SummaryMinRequest(
            instrument_ids=[1],
        ))
        print(response)


if __name__ == "__main__":
    unittest.main()
