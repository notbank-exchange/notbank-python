from typing import List
import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.models.level2_ticker_snapshot import Level2TickerSnapshot
from notbank_python_sdk.requests_models.get_l2_snapshot import GetL2SnapshotRequest
from tests import test_helper


class TestGetL2Snapshot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_l2_snapshot_success(self):
        request = GetL2SnapshotRequest(
            instrument_id=1,
            depth=10
        )
        response = self.client.get_l2_snapshot(request)
        self.assertIsInstance(response, List[Level2TickerSnapshot])
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0].md_update_id, 26)
        self.assertEqual(response[0].price, 28700)
        self.assertEqual(response[0].side, 0)


if __name__ == "__main__":
    unittest.main()
