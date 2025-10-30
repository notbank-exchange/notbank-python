import unittest
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import DownloadDocumentSliceRequest
from tests import test_helper


class TestDownloadDocumentSlice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_download_document_slice_success(self):
        response = self.client.download_document_slice(DownloadDocumentSliceRequest(
            "66769552-cacd-471b-bb53-04b1ed1c87f9", 0))


if __name__ == "__main__":
    unittest.main()
