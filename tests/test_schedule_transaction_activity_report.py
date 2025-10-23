import unittest
from notbank_python_sdk.constants import ReportFrequency
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import ScheduleTransactionActivityReportRequest
from tests import test_helper


class TestScheduleTransactionActivityReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(print)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_schedule_transaction_activity_report_success(self):
        response = self.client.schedule_transaction_activity_report(ScheduleTransactionActivityReportRequest(
            begin_time="2023-03-30T16:00:00.000Z",
            account_id_list=[self.credentials.account_id],
            frequency=ReportFrequency.MONTHLY,
        ))
        print(response)


if __name__ == "__main__":
    unittest.main()
