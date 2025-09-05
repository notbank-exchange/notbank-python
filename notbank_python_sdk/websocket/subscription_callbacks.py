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
        callback = self._callbacks.get(callback_id)
        if callback is not None:
            return callback
        last_suffix_start = callback_id.rfind("_")
        if last_suffix_start == -1:
            return None
        reduced_callback_id = callback_id[0:last_suffix_start]
        return self._callbacks.get(reduced_callback_id)

    def remove(self, callback_id: str) -> None:
        if callback_id in self._callbacks:
            del self._callbacks[callback_id]

    def close(self) -> None:
        self._callbacks.clear()
