import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import GetUserDevicesRequest
from tests import test_helper


class TestGetUserDevices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_user_devices_success(self):
        response = self.client.get_user_devices(
            GetUserDevicesRequest(user_id=self.credentials.user_id))


if __name__ == "__main__":
    unittest.main()
