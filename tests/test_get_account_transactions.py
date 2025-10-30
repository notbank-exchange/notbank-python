import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.models.account_transaction import (
    TransactionType,
    TransactionReferenceType,
)
from notbank_python_sdk.requests_models import GetAccountTransactionsRequest
from tests import test_helper


class TestGetAccountTransactions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_transaction(self):
        response = self.client.get_account_transactions(GetAccountTransactionsRequest(
            account_id=self.credentials.account_id,
            transaction_id=15515083
        ))
        self.assertEqual(len(response), 1)
        
    def test_get_transactions(self):
        response = self.client.get_account_transactions(GetAccountTransactionsRequest(
            account_id=self.credentials.account_id,
            transaction_reference_types=[TransactionReferenceType.DEPOSIT,TransactionReferenceType.WITHDRAW],
            product_id=3
        ))
        self.assertEqual(len(response), 1)

    def test_no_transactions_found(self):
        request = GetAccountTransactionsRequest(account_id=999)
        response = self.client.get_account_transactions(request)
        self.assertEqual(len(response), 0)


if __name__ == "__main__":
    unittest.main()
