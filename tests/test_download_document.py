import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.download_document import DownloadDocumentRequest
from tests import test_helper


class TestDownloadDocument(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_download_document_success(self):
        req = DownloadDocumentRequest("66769552-cacd-471b-bb53-04b1ed1c87f9")
        res = self.client.download_document(req)
        self.assertEqual(res.descriptor_id,
                         "66769552-cacd-471b-bb53-04b1ed1c87f9")
        self.assertEqual(res.status_code, "Success")
        self.assertEqual(res.status_message, "success")
        self.assertTrue(res.doc_name.endswith(".csv"))
        self.assertEqual(res.num_slices, 1)

    def test_download_document_error(self):
        req = DownloadDocumentRequest("invalid-guid")
        res = self.client.download_document(req)
        self.assertEqual(res.status_code, "Error")
        self.assertEqual(res.status_message, "error")
        self.assertEqual(res.doc_name, "")
        self.assertEqual(res.num_slices, 0)


if __name__ == "__main__":
    unittest.main()
