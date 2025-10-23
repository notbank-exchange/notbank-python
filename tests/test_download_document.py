import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.download_document import DownloadDocumentRequest
from tests import test_helper


class TestDownloadDocument(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(print, print)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_download_document_success(self):
        response = self.client.download_document(DownloadDocumentRequest("3108e502-ba32-f2b0-73b3-ffb0bd997390"))
    
if __name__ == "__main__":
    unittest.main()
