from time import sleep
import unittest

from dacite import from_dict, Config
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.models.pong import Pong
from tests import test_helper


class TestPing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_websocket_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_ping(self):
        self.client.ping()
        self.client.close()


if __name__ == "__main__":
    unittest.main()
