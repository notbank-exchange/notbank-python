from decimal import Decimal
import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import OmsFeesRequest
from tests import test_helper


class TestGetOmsWithdrawFees(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_oms_withdraw_fees(self):
        response = self.client.get_oms_deposit_fees(OmsFeesRequest(
            product_id=1,
            account_provider_id=8,
        ))
        print(response)


if __name__ == "__main__":
    unittest.main()
