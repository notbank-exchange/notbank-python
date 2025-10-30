import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import CancelUserReportRequest
from tests import test_helper


class TestCancelUserReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_cancel_user_report(self):
        response = self.client.cancel_user_report(CancelUserReportRequest(
            user_report_id="ff4b0469-17e9-49d5-bffc-ce137508a454"))
        print(response)


if __name__ == "__main__":
    unittest.main()
