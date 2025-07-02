import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.models.account_transaction import (
    TransactionType,
    TransactionReferenceType,
)
from notbank_python_sdk.requests_models.get_account_transactions_request import (
    GetAccountTransactionsRequest,
)
from tests import test_helper


class TestGetAccountTransactions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_transactions_success(self):
        """Prueba exitosa: obtención de transacciones válidas."""
        request = GetAccountTransactionsRequest(
            account_id=7, depth=2, product_id=3
        )
        response = self.client.get_account_transactions(request)

        self.assertEqual(len(response), 2)
        self.assertEqual(response[0].transaction_id, 24214)
        self.assertEqual(response[0].cr, 0.01247667)
        self.assertEqual(response[0].dr, 0.0)
        self.assertEqual(response[0].transaction_type, TransactionType.trade)
        self.assertEqual(response[0].reference_type,
                         TransactionReferenceType.trade)
        self.assertEqual(response[1].transaction_id, 24215)
        self.assertEqual(response[1].transaction_type, TransactionType.trade)

    def test_no_transactions_found(self):
        """Prueba: No se encuentran transacciones en la cuenta."""
        request = GetAccountTransactionsRequest(account_id=999)
        response = self.client.get_account_transactions(request)
        self.assertEqual(len(response), 0)

    def test_invalid_omsid(self):
        """Prueba fallida: oms_id inválido."""
        request = GetAccountTransactionsRequest(account_id=7)
        with self.assertRaises(ValueError):
            self.client.get_account_transactions(request)


if __name__ == "__main__":
    unittest.main()
