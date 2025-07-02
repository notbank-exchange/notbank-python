from time import sleep
import unittest

from notbank_python_sdk.requests_models.subscribe_level2_request import SubscribeLevel2Request
from notbank_python_sdk.requests_models.subscribe_ticker_request import SubscribeTickerRequest
from notbank_python_sdk.requests_models.unsubscribe_ticker_request import UnsubscribeTickerRequest
from notbank_python_sdk.notbank_client import NotbankClient
from tests.test_helper import CallMarker, new_websocket_client_connection


class TestSubscribeTicker(unittest.TestCase):
    def setUp(self):
        self._websocket_connection = new_websocket_client_connection()
        self._websocket_connection.connect()
        self._system_client = NotbankClient(self._websocket_connection)

    def test_subscribe_with_instrument_id(self):
        snapshot_marker = CallMarker.create()
        update_marker = CallMarker.create()

        self._system_client.subscribe_ticker(
            SubscribeTickerRequest(154, 60, 3),
            lambda ticker: snapshot_marker.mark_called(),
            lambda ticker: update_marker.mark_called())
        sleep(70)
        self._system_client.unsubscribe_ticker(
            UnsubscribeTickerRequest(154))
        sleep(3)
        self._websocket_connection.close()
        self.assertTrue(snapshot_marker.was_callled(),
                        'snapshot callback was not called')
        self.assertTrue(update_marker.was_callled(),
                        'update callback was not called')


if __name__ == "__main__":
    unittest.main()
