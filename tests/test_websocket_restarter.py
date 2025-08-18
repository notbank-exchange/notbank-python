import threading
from time import sleep
import logging
import unittest

from notbank_python_sdk.client_connection_factory import new_restarting_websocket_client_connection as create_restarting_websocket_client_connection
from notbank_python_sdk.requests_models.authenticate_request import AuthenticateRequest

from notbank_python_sdk.notbank_client import NotbankClient
from tests.test_helper import load_credentials, TEST_URL


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
        self._websocket_connection = new_restarting_websocket_client_connection()
        self._websocket_connection.connect()
        self._client = NotbankClient(self._websocket_connection)

    def test_restart_websocket(self):
        credentials = load_credentials()
        self._client.authenticate(AuthenticateRequest(
            credentials.public_key, credentials.secret_key, credentials.user_id))
        while True:
            sleep(10)
            print("threads", [
                  thread.name for thread in threading.enumerate()], "\n")


if __name__ == "__main__":
    unittest.main()
