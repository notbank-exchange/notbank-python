import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.cancel_order import CancelOrder
from tests import test_helper


class TestSendCancelList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_send_cancel_list_success(self):
        self.client.send_cancel_list([
            CancelOrder(
                order_id=6714,
                account_id=9,
            ),
            CancelOrder(
                order_id=6507,
                account_id=9,
            ),
        ])


if __name__ == "__main__":
    unittest.main()
