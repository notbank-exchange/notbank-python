from typing import Any, Dict, List
from notbank_python_sdk.websocket.subscription import Subscription, Unsubscription
from notbank_python_sdk.websocket.websocket_connection import WebsocketConnection


class Resubscriber:
    _id: int
    _active_suscriptions: Dict[int, Subscription[Any]]

    def __init__(self):
        self._id = 0
        self._active_suscriptions = {}

    def save(self, subscription: Subscription[Any]) -> None:
        self._id += 1
        current_id = self._id
        self._active_suscriptions[current_id] = subscription

    def remove(self, unsubscription: Unsubscription[Any]) -> None:
        for callback_id in unsubscription.callback_ids:
            for sub_id in self._active_suscriptions:
                for active_callback in self._active_suscriptions[sub_id].callbacks:
                    if active_callback.id == callback_id:
                        del self._active_suscriptions[sub_id]
                        return

    def _get_subscriptions(self) -> List[Subscription[Any]]:
        return list(self._active_suscriptions.values())

    def resubscribe(self, connection: WebsocketConnection) -> None:
        for subscription in self._get_subscriptions():
            connection.subscribe(subscription)
