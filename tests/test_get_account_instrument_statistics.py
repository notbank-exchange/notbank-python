import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_account_instrument_statistics_request import GetAccountInstrumentStatisticsRequest
from tests import test_helper


class TestGetAccountInstrumentStatistics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_account_instrument_statistics_success(self):
        """Prueba exitosa: estadísticas válidas."""
        request = GetAccountInstrumentStatisticsRequest(
            account_id=7,
        )
        response = self.client.get_account_instrument_statistics(request)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0].instrument_symbol, "BTCUSD")
        self.assertEqual(response[1].instrument_symbol, "ETHUSD")
        self.assertEqual(response[0].monthly_quantity_bought, 0.1602)
        self.assertEqual(response[1].total_month_buys, 6)

    def test_get_account_instrument_statistics_not_found(self):
        """Prueba: account_id inválido, no se encuentra estadísticas."""
        request = GetAccountInstrumentStatisticsRequest(
            account_id=999,
        )
        response = self.client.get_account_instrument_statistics(request)
        self.assertEqual(len(response), 0)


if __name__ == "__main__":
    unittest.main()
