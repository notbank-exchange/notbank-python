import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.cancel_user_report import CancelUserReportRequest
from tests import test_helper


class TestCancelUserReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)
        
    def test_cancel_user_report_success(self):
        req = CancelUserReportRequest(user_report_id="389f244a-b958-4545-a4a7-61a73205b59e")
        self.client.cancel_user_report(req)
        

    def test_cancel_user_report_not_authorized(self):
        req = CancelUserReportRequest(user_report_id="no-perm-guid")
        self.client.cancel_user_report(req)

if __name__ == "__main__":
    unittest.main()
