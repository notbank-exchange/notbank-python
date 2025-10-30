import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import GetUserReportWriterResultRecordsRequest
from tests import test_helper


class TestGetUserReportWriterResultRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(print)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_user_report_writer_result_records_success(self):
        response = self.client.get_user_report_writer_result_records(
            GetUserReportWriterResultRecordsRequest(user_id=self.credentials.user_id))
        print(response)


if __name__ == "__main__":
    unittest.main()
