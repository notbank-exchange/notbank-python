import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import GetAccountInstrumentStatisticsRequest
from tests import test_helper


class TestGetAccountInstrumentStatistics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_account_instrument_statistics_success(self):
        response = self.client.get_account_instrument_statistics(GetAccountInstrumentStatisticsRequest(
            account_id=7,
        ))

    def test_get_account_instrument_statistics_not_found(self):
        request = GetAccountInstrumentStatisticsRequest(
            account_id=99999,
        )
        response = self.client.get_account_instrument_statistics(request)
        self.assertEqual(len(response), 0)


if __name__ == "__main__":
    unittest.main()
