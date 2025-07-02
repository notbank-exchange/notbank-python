
import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.generate_product_delta_activity_report import GenerateProductDeltaActivityReportRequest
from tests import test_helper


class TestGenerateProductDeltaActivityReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_generate_product_delta_activity_report_success(self):
        request = GenerateProductDeltaActivityReportRequest(
            start_time="2023-03-01T16:00:00.000Z",
            end_time="2023-03-02T16:00:00.000Z",
            account_id_list=[185, 9],
        )
        response = self.client.generate_product_delta_activity_report(request)
        self.assertEqual(response.requesting_user, 1)
        self.assertEqual(response.oms_id, 1)
        self.assertEqual(response.report_flavor, "ProductDelta")
        self.assertEqual(response.request_status, "Submitted")
        self.assertEqual(response.account_ids, [9, 185])

    def test_generate_product_delta_activity_report_empty_accounts(self):
        request = GenerateProductDeltaActivityReportRequest(
            start_time="2024-01-01T00:00:00.000Z",
            end_time="2024-01-02T00:00:00.000Z",
            account_id_list=[],
        )
        response = self.client.generate_product_delta_activity_report(request)
        self.assertEqual(response.account_ids, [])
        self.assertEqual(response.request_status, "Submitted")
        self.assertEqual(response.report_flavor, "ProductDelta")

    def test_generate_product_delta_activity_report_invalid_oms(self):
        request = GenerateProductDeltaActivityReportRequest(
            start_time="2024-01-01T00:00:00.000Z",
            end_time="2024-01-02T00:00:00.000Z",
            account_id_list=[1],
        )
        with self.assertRaises(Exception) as context:
            self.client.generate_product_delta_activity_report(request)
        self.assertIn("Invalid OMSId", str(context.exception))


if __name__ == "__main__":
    unittest.main()
