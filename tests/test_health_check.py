from time import sleep
import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from tests import test_helper


class TestHealthCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_health_check(self):
        self.client.health_check()
        self.client.close()


if __name__ == "__main__":
    unittest.main()
