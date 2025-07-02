import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_user_permissions import GetUserPermissionsRequest
from tests import test_helper


class TestGetUserPermissions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_user_permissions_success(self):
        req = GetUserPermissionsRequest(user_id=6)
        res = self.client.get_user_permissions(req)
        self.assertEqual(res, [
                         "Deposit", "Operator", "Trading", "Withdraw"])

    def test_get_user_permissions_empty(self):
        req = GetUserPermissionsRequest(user_id=999)
        res = self.client.get_user_permissions(req)
        self.assertEqual(res, [])


if __name__ == "__main__":
    unittest.main()
