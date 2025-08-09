from time import sleep
import logging
import unittest

from notbank_python_sdk.client_connection_factory import new_restarting_websocket_client_connection as create_restarting_websocket_client_connection
from notbank_python_sdk.requests_models.subscribe_level1_request import SubscribeLevel1Request
from notbank_python_sdk.requests_models.subscribe_level2_request import SubscribeLevel2Request
from notbank_python_sdk.requests_models.unsubscribe_level1_request import UnsubscribeLevel1Request
from notbank_python_sdk.notbank_client import NotbankClient
from tests.test_helper import CallMarker, new_websocket_client_connection, TEST_URL


def new_restarting_websocket_client_connection():
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    return create_restarting_websocket_client_connection(
        TEST_URL,
        lambda: logger.debug("on open"),
        lambda o1, o2: logger.debug("on close"),
        lambda err: logger.debug("error: " + str(err)),
        lambda msg: logger.debug("message in: " + msg),
        lambda msg: logger.debug("message out: "+msg),
        5)


class TestWebsocketRestarter(unittest.TestCase):
    def setUp(self):
        self._websocket_connection = new_websocket_client_connection()
        self._websocket_connection.connect()
        self._system_client = NotbankClient(self._websocket_connection)

    def test_restart_websocket(self):
        snapshot_marker = CallMarker.create()
        update_marker = CallMarker.create()

        self._system_client.subscribe_level_2(
            SubscribeLevel2Request(10, symbol="ETHBTC"),
            lambda level_2: snapshot_marker.mark_called(),
            lambda level_2: update_marker.mark_called())
        sleep(14)
        sleep(3)
        self._websocket_connection.close()
        self.assertTrue(
            snapshot_marker.was_callled(),
            'snapshot callback was not called')
        self.assertTrue(
            update_marker.was_callled(),
            'snapshot callback was not called')


if __name__ == "__main__":
    unittest.main()
