import unittest
from notbank_python_sdk.requests_models.get_account_info_request import GetAccountInfoRequest
from notbank_python_sdk.requests_models.update_one_step_withdraw_request import Action, UpdateOneStepWithdrawRequest

from tests import test_helper

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.get_banks_request import GetBanksRequest


class TestUpdateOneStepWithdraw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_update_one_step_withdraw(self):
        response = self.client.update_one_step_withdraw(
            UpdateOneStepWithdrawRequest(self.credentials.account_id, Action.ENABLE, "044378"))
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
