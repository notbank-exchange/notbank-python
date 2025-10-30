import unittest
from notbank_python_sdk.requests_models import GetOwnersFiatWithdrawRequest


from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient


class TestCreateFiatDeposit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_create_fiat_deposit(self):
        self.client.get_owners_fiat_withdraw(GetOwnersFiatWithdrawRequest(
            cbu="6845784411100069899422"
        ))


if __name__ == "__main__":
    unittest.main()
