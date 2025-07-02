import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_user_report_tickets import GetUserReportTicketsRequest
from tests import test_helper


class TestGetUserReportTickets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_user_report_tickets_success(self):
        req = GetUserReportTicketsRequest(user_id=6)
        result = self.client.get_user_report_tickets(req)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        r = result[0]
        self.assertEqual(r.requesting_user, 6)
        self.assertEqual(r.report_flavor, "TradeActivity")
        self.assertEqual(r.account_ids, [9])

    def test_get_user_report_tickets_no_results(self):
        req = GetUserReportTicketsRequest(user_id=99)
        result = self.client.get_user_report_tickets(req)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
