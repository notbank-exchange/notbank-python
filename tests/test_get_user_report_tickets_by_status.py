import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_user_report_tickets_by_status import GetUserReportTicketsByStatusRequest
from tests import test_helper


class TestGetUserReportTicketsByStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_user_report_tickets_by_status_multiple(self):
        req = GetUserReportTicketsByStatusRequest(
            request_statuses=["Submitted", "Scheduled"])
        res = self.client.get_user_report_tickets_by_status(req)
        self.assertIsInstance(res, list)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0].request_status, "Submitted")
        self.assertEqual(res[1].request_status, "Scheduled")
        self.assertEqual(res[1].account_ids, [32])

    def test_get_user_report_tickets_by_status_none(self):
        req = GetUserReportTicketsByStatusRequest()
        res = self.client.get_user_report_tickets_by_status(req)
        self.assertEqual(res, [])


if __name__ == "__main__":
    unittest.main()
