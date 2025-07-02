from time import sleep
import unittest

from notbank_python_sdk.requests_models.subscribe_level1_request import SubscribeLevel1Request
from notbank_python_sdk.requests_models.unsubscribe_level1_request import UnsubscribeLevel1Request
from notbank_python_sdk.notbank_client import NotbankClient
from tests.test_helper import CallMarker, new_websocket_client_connection


class TestSubscribeLevel1Ticker(unittest.TestCase):
    def setUp(self):
        self._websocket_connection = new_websocket_client_connection()
        self._websocket_connection.connect()
        self._system_client = NotbankClient(self._websocket_connection)

    def test_subscribe_with_instrument_id(self):
        snapshot_marker = CallMarker.create()

        self._system_client.subscribe_level_1(
            SubscribeLevel1Request(154),
            lambda ticker: snapshot_marker.mark_called(),
            lambda ticker: None)
        sleep(14)
        self._system_client.unsubscribe_level_1(
            UnsubscribeLevel1Request(154))
        sleep(3)
        self._websocket_connection.close()
        self.assertTrue(snapshot_marker.was_callled(),
                        'snapshot callback was not called')


if __name__ == "__main__":
    unittest.main()
