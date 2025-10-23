import unittest
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.get_user_report_tickets import GetUserReportTicketsRequest


from notbank_python_sdk.requests_models.remove_user_report_ticket import RemoveUserReportTicketRequest
from tests import test_helper


class TestRemoveUserReportTicket(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(print, print)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_remove_user_report_ticket_success(self):
      self.client.remove_user_report_ticket(RemoveUserReportTicketRequest(
            "18066e61-5adf-61be-1203-eacbe6bb8905"))


if __name__ == "__main__":
    unittest.main()
