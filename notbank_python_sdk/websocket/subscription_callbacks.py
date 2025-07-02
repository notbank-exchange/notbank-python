from typing import Callable, Dict, Optional


class SubscriptionCallbacks:
    _callbacks: Dict[str,  Callable[[str], None]]

    def __init__(self, callbacks: Dict[str,  Callable[[str], None]]):
        self._callbacks = callbacks

    @staticmethod
    def create():
        return SubscriptionCallbacks({})

    def add(self,  callback_id: str, handler: Callable[[str], None]) -> None:
        self._callbacks[callback_id] = handler

    def get(self, callback_id: str) -> Optional[Callable[[str], None]]:
        return self._callbacks.get(callback_id)

    def remove(self, callback_id: str) -> None:
        if callback_id in self._callbacks:
            del self._callbacks[callback_id]

    def close(self) -> None:
        self._callbacks.clear()
