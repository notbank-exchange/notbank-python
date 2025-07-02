from time import sleep
import unittest

from notbank_python_sdk.requests_models.subscribe_level2_request import SubscribeLevel2Request
from notbank_python_sdk.requests_models.unsubscribe_level2_request import UnsubscribeLevel2Request
from notbank_python_sdk.notbank_client import NotbankClient
from tests.test_helper import CallMarker, new_websocket_client_connection


class TestSubscribeLevel2Ticker(unittest.TestCase):
    def setUp(self):
        self._websocket_connection = new_websocket_client_connection()
        self._websocket_connection.connect()
        self._system_client = NotbankClient(self._websocket_connection)

    def test_subscribe_with_instrument_id(self):
        snapshot_marker = CallMarker.create()
        update_marker = CallMarker.create()

        def handle_snapshot():
            snapshot_marker.mark_called()
            print("snapshot n: "+str(snapshot_marker.get_call_count()))

        def handle_update():
            update_marker.mark_called()
            print("update n: " + str(update_marker.get_call_count()))

        self._system_client.subscribe_level_2(
            SubscribeLevel2Request(10, 154),
            lambda tickers: handle_snapshot(),
            lambda tickers: handle_update())
        sleep(80)
        self._system_client.unsubscribe_level_2(
            UnsubscribeLevel2Request(154))
        sleep(3)
        self._websocket_connection.close()
        self.assertTrue(snapshot_marker.was_callled(),
                        'snapshot callback was not called')
        self.assertTrue(update_marker.was_callled(),
                        'update callback was not called')


if __name__ == "__main__":
    unittest.main()
