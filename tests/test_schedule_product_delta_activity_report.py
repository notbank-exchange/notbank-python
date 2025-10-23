import unittest
from notbank_python_sdk.constants import ReportFrequency
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models import ScheduleProductDeltaActivityReportRequest
from tests import test_helper


class TestScheduleProductDeltaActivityReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_schedule_product_delta_activity_report_success(self):
        response = self.client.schedule_product_delta_activity_report(ScheduleProductDeltaActivityReportRequest(
            begin_time="2023-03-30T16:00:00.000Z",
            account_id_list=[self.credentials.account_id],
            frequency=ReportFrequency.WEEKLY,
        ))
        print(response)


if __name__ == "__main__":
    unittest.main()
