import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from tests import test_helper


class TestGetEnums(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_enums_success(self):
        response = self.client.get_enums()
        self.assertIsInstance(response, list)
        self.assertGreaterEqual(len(response), 1)
        self.assertEqual(response[0].class_name, "Order")
        self.assertEqual(response[0].property_name, "OrderState")
        self.assertEqual(len(response[0].enums), 2)
        self.assertEqual(response[0].enums[0].name, "Working")
        self.assertEqual(response[0].enums[1].number, 2)


if __name__ == "__main__":
    unittest.main()
