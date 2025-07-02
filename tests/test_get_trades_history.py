from decimal import Decimal
import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_trades_history import GetTradesHistoryRequest
from tests import test_helper


class TestGetTradesHistory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_trades_history_success(self):
        """Prueba exitosa: oms_id y account_id válidos."""
        request = GetTradesHistoryRequest(account_id=7)
        response = self.client.get_trades_history(request)

        # Verificar que devuelve correctamente 1 trade
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].trade_id, 964)
        self.assertEqual(response[0].price, Decimal(6000.0))

    def test_get_trades_history_not_found(self):
        """Prueba: account_id inválido, no se encuentra el registro."""
        request = GetTradesHistoryRequest(account_id=999)
        response = self.client.get_trades_history(request)

        # Verificar que no se devuelven trades
        self.assertEqual(len(response), 0)


# Punto de entrada para ejecutar pruebas
if __name__ == "__main__":
    unittest.main()
