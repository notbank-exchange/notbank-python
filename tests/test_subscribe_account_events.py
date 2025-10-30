from time import sleep
import unittest

from notbank_python_sdk.requests_models import UnsubscribeTradesRequest
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import SubscribeAccountEventsRequest
from notbank_python_sdk.requests_models.unsubscribe_account_events_request import UnsubscribeAccountEventsRequest
from tests import test_helper
from tests.test_helper import CallMarker, new_websocket_client_connection


def handler(some):
    print(some)


class TestSubscribeAccountEvents(unittest.TestCase):
    def setUp(self):
        self.connection = new_websocket_client_connection()
        self.connection.connect()
        self.client = NotbankClient(self.connection)
        self.credentials = test_helper.load_credentials()

    def test_subscribe_account_events(self):
        self.client.subscribe_account_events(
            SubscribeAccountEventsRequest(self.credentials.account_id),
            lambda ticket: print("withdraw ticket", ticket),
            lambda transaction: print("transaction", transaction),
            lambda trade: print("trade", trade),
            lambda order: print("order", order),
            lambda ticket: print("ticket", ticket),
            lambda account: print("account", account),
            lambda deposit: print("deposit_ ticket", deposit),
            lambda cancel_order_reject_event: print(
                "cancel order reject event", cancel_order_reject_event),
            lambda account_position: print(
                "account position", account_position)
        )
        sleep(60)
        self.client.unsubscribe_account_events(
            UnsubscribeAccountEventsRequest(self.credentials.account_id))
        self.connection.close()


if __name__ == "__main__":
    unittest.main()
