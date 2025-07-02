import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.user_devices import GetUserDevicesRequest
from tests import test_helper


class TestGetUserDevices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_user_devices_success(self):
        request = GetUserDevicesRequest(user_id=6)
        response = self.client.get_user_devices(request)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0].hash_code, 345283502)
        self.assertEqual(response[1].is_trusted, True)

    def test_get_user_devices_no_results(self):
        request = GetUserDevicesRequest(user_id=100)
        response = self.client.get_user_devices(request)
        self.assertIsInstance(response, list)
        self.assertEqual(response, [])

    def test_get_user_devices_no_param(self):
        # Simula la consulta de dispositivos para el usuario autenticado
        request = GetUserDevicesRequest()
        response = self.client.get_user_devices(request)
        self.assertIsInstance(response, list)
        self.assertGreaterEqual(len(response), 1)
        self.assertEqual(response[0].device_name, "Mac OS X 10.15")
        self.assertTrue(response[0].is_trusted)


if __name__ == "__main__":
    unittest.main()
