import unittest
from notbank_python_sdk.requests_models.create_bank_account_request import CreateBankAccountRequest
from notbank_python_sdk.requests_models.delete_bank_account_request import DeleteBankAccountRequest
from notbank_python_sdk.requests_models.get_bank_account_request import GetBankAccountRequest
from notbank_python_sdk.requests_models.get_bank_accounts_request import GetBankAccountsRequest

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient


class TestGetBanks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_account_flow(self):
        account = self.client.create_bank_account(
            CreateBankAccountRequest("CLP", "123", "1212", "kind"))
        print(account)
        try:
            self.client.get_bank_account(
                GetBankAccountRequest(account.id))
            accounts = self.client.get_bank_accounts(GetBankAccountsRequest())
            filtered_accounts = list(filter(
                lambda an_account: an_account.id == account.id, accounts.data))
            if len(filtered_accounts) != 1:
                print("account not fetched")
        except Exception as e:
            print(e)
        self.client.delete_bank_account(DeleteBankAccountRequest(account.id))


if __name__ == "__main__":
    unittest.main()
