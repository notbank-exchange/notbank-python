import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.schedule_trade_activity_report import ScheduleTradeActivityReportRequest
from tests import test_helper


class TestScheduleTradeActivityReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)


    def test_schedule_trade_activity_report_success(self):
        request = ScheduleTradeActivityReportRequest(
            begin_time="2023-03-30T16:00:00.000Z",
            account_id_list=[185, 9],
            frequency="Weekly",
        )
        response = self.client.schedule_trade_activity_report(request)
        self.assertEqual(response.requesting_user, 6)
        self.assertEqual(response.oms_id, 1)
        self.assertEqual(response.report_flavor, "TradeActivity")
        self.assertEqual(response.request_status, "Submitted")
        self.assertEqual(response.account_ids, [9, 185])
        self.assertEqual(response.report_frequency, "Weekly")

    def test_schedule_trade_activity_report_empty_accounts(self):
        request = ScheduleTradeActivityReportRequest(
            begin_time="2024-01-01T00:00:00.000Z",
            account_id_list=[],
            frequency="Monthly",
        )
        response = self.client.schedule_trade_activity_report(request)
        self.assertEqual(response.account_ids, [])
        self.assertEqual(response.request_status, "Submitted")
        self.assertEqual(response.report_flavor, "TradeActivity")
        self.assertEqual(response.report_frequency, "Monthly")

    def test_schedule_trade_activity_report_invalid_oms(self):
        request = ScheduleTradeActivityReportRequest(
            begin_time="2024-01-01T00:00:00.000Z",
            account_id_list=[1],
            frequency="Daily",
        )
        with self.assertRaises(Exception) as context:
            self.client.schedule_trade_activity_report(request)
        self.assertIn("Invalid OMSId", str(context.exception))

if __name__ == "__main__":
    unittest.main()
