from time import sleep
import unittest

from notbank_python_sdk.requests_models import SubscribeTradesRequest
from notbank_python_sdk.requests_models import UnsubscribeTradesRequest
from notbank_python_sdk.notbank_client import NotbankClient
from tests.test_helper import CallMarker, new_websocket_client_connection


class TestSubscribeTrades(unittest.TestCase):
    def setUp(self):
        self.connection = new_websocket_client_connection()
        self.connection.connect()
        self.client = NotbankClient(self.connection)

    def test_subscribe_with_instrument_id(self):
        snapshot_marker = CallMarker.create()
        update_marker = CallMarker.create()

        self.client.subscribe_trades(
            SubscribeTradesRequest(154, 3),
            lambda trades: snapshot_marker.mark_called(),
            lambda trades: update_marker.mark_called())
        sleep(60)
        self.client.unsubscribe_trades(UnsubscribeTradesRequest(154))
        self.connection.close()
        self.assertTrue(snapshot_marker.was_callled(),
                        'snapshot callback was not called')
        self.assertTrue(update_marker.was_callled(),
                        'update callback was not called')


if __name__ == "__main__":
    unittest.main()
