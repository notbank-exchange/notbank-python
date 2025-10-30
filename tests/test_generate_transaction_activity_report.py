import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.generate_transaction_activity_report import GenerateTransactionActivityReportRequest
from tests import test_helper


class TestGenerateTransactionActivityReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_generate_transaction_activity_report_success(self):
        response = self.client.generate_transaction_activity_report(GenerateTransactionActivityReportRequest(
            start_time="2023-03-01T16:00:00.000Z",
            end_time="2023-03-02T16:00:00.000Z",
            account_id_list=[self.credentials.account_id],
        ))
        print(response)
        

if __name__ == "__main__":
    unittest.main()
