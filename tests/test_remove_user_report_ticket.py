import unittest
from notbank_python_sdk.notbank_client import NotbankClient


from notbank_python_sdk.requests_models.remove_user_report_ticket import RemoveUserReportTicketRequest
from tests import test_helper


class TestRemoveUserReportTicket(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_remove_user_report_ticket_success(self):
        req = RemoveUserReportTicketRequest(
            "e27e5268-db50-70fa-de84-ee0b6ae16093")
        self.client.remove_user_report_ticket(req)

    def test_remove_user_report_ticket_failure(self):
        req = RemoveUserReportTicketRequest(
            '{"user_report_ticket_id": "bad-format"}')
        self.client.remove_user_report_ticket(req)


if __name__ == "__main__":
    unittest.main()
