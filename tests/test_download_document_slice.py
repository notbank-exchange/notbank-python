import unittest
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.download_document_slice import DownloadDocumentSliceRequest
from tests import test_helper


class TestDownloadDocumentSlice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_download_document_slice_success(self):
        req = DownloadDocumentSliceRequest(
            "66769552-cacd-471b-bb53-04b1ed1c87f9", 0)
        res = self.client.download_document_slice(req)
        self.assertEqual(res.descriptor_id,
                         "66769552-cacd-471b-bb53-04b1ed1c87f9")
        self.assertEqual(res.status_code, "Success")
        self.assertEqual(res.status_message, "Success")
        self.assertTrue(len(res.base64_bytes) > 0)

    def test_download_document_slice_error(self):
        req = DownloadDocumentSliceRequest("invalid-guid", 1)
        res = self.client.download_document_slice(req)
        self.assertEqual(res.status_code, "Error")
        self.assertEqual(res.status_message, "error")
        self.assertEqual(res.base64_bytes, "")


if __name__ == "__main__":
    unittest.main()
