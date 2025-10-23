import unittest
from notbank_python_sdk.constants import ReportRequestStatus
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import GetUserReportTicketsByStatusRequest
from tests import test_helper


class TestGetUserReportTicketsByStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(print, print)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_user_report_tickets_by_status_multiple(self):
        response = self.client.get_user_report_tickets_by_status(GetUserReportTicketsByStatusRequest(
            request_statuses=[ReportRequestStatus.SUBMITTED, ReportRequestStatus.SCHEDULED]))
        print(response)


if __name__ == "__main__":
    unittest.main()
