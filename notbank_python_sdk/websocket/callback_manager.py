from typing import Callable, TypeVar, Generic, List

from notbank_python_sdk.websocket.message_frame import MessageFrame
from .sequenced_callbacks import SequencedCallbacks
from .subscription_callbacks import SubscriptionCallbacks

T = TypeVar('T')


class CallbackManager:
    sequenced_callbacks: SequencedCallbacks[MessageFrame]
    subscription_callbacks: SubscriptionCallbacks

    def __init__(self, sequenced_callbacks: SequencedCallbacks[MessageFrame], subscription_callbacks: SubscriptionCallbacks):
        self.sequenced_callbacks = sequenced_callbacks
        self.subscription_callbacks = subscription_callbacks

    @staticmethod
    def create() -> 'CallbackManager':
        return CallbackManager(SequencedCallbacks.create(), SubscriptionCallbacks.create())

    def close(self) -> None:
        self.sequenced_callbacks.close()
        self.subscription_callbacks.close()
