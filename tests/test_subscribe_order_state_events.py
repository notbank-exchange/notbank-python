from time import sleep
import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import SubscribeOrderStateEventsRequest
from notbank_python_sdk.requests_models import UnsubscribeOrderStateEventsRequest
from tests import test_helper
from tests.test_helper import CallMarker, new_websocket_client_connection


def handler(some):
    print(some)


class TestSubscribeOrderStateEvents(unittest.TestCase):
    def setUp(self):
        self.connection = new_websocket_client_connection()
        self.connection.connect()
        self.client = NotbankClient(self.connection)
        self.credentials = test_helper.load_credentials()

    def test_subscribe_account_events(self):
        self.client.subscribe_order_state_events(
          SubscribeOrderStateEventsRequest(self.credentials.account_id, instrument_id=99),
          lambda event: print(event))
        sleep(60)
        self.client.unsubscribe_order_state_events(UnsubscribeOrderStateEventsRequest(7))
        self.connection.close()


if __name__ == "__main__":
    unittest.main()
