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
        """
        Prueba exitosa: solicitud válida, devuelve 'True'.
        """
        request = [
            CancelOrder(
                order_id=6714,
                account_id=9,
            ),
            CancelOrder(
                order_id=6507,
                account_id=9,
            ),
        ]

        self.client.send_cancel_list(request)

    def test_send_cancel_list_empty_list(self):
        """
        Prueba: lista vacía, devuelve 'False' con mensaje de error.
        """
        request = []
        self.client.send_cancel_list(request)


if __name__ == "__main__":
    unittest.main()
