import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_order_status import GetOrderStatusRequest
from tests import test_helper


class TestGetOrderStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_order_status_success(self):
        response = self.client.get_order_status(GetOrderStatusRequest(
            account_id=7,
            order_id=6562,
        ))



if __name__ == "__main__":
    unittest.main()
