import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_user_report_writer_result_records import GetUserReportWriterResultRecordsRequest
from tests import test_helper


class TestGetUserReportWriterResultRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_user_report_writer_result_records_success(self):
        req = GetUserReportWriterResultRecordsRequest(user_id=6)
        result = self.client.get_user_report_writer_result_records(req)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        r = result[0]
        self.assertEqual(r.requesting_user, 6)
        self.assertEqual(r.result_status, "SuccessComplete")
        self.assertTrue("TradeActivity" in r.report_descriptive_header)

    def test_get_user_report_writer_result_records_no_results(self):
        req = GetUserReportWriterResultRecordsRequest(user_id=99)
        result = self.client.get_user_report_writer_result_records(req)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
