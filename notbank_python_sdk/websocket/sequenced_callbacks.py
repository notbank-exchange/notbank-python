from typing import Callable, Dict, Generic, Optional, TypeVar

T = TypeVar('T')


class SequencedCallbacks(Generic[T]):
    _sequence_number: int
    _callbacks: Dict[int, Callable[[T], None]]

    def __init__(self, sequence_number: int, callbacks: Dict[int, Callable[[T], None]]):
        self._sequence_number = sequence_number
        self._callbacks = callbacks

    @staticmethod
    def create() -> "SequencedCallbacks":
        return SequencedCallbacks(sequence_number=2, callbacks={})

    def pop(self, sequence_number: int) -> Optional[Callable[[T], None]]:
        return self._callbacks.pop(sequence_number, None)

    def put(self, callback: Callable[[T], None]) -> int:
        sequence_number = self._get_next_sequence_number()
        self._callbacks[sequence_number] = callback
        return sequence_number

    def _get_next_sequence_number(self) -> int:
        sequence_number = self._sequence_number
        self._sequence_number += 2
        return sequence_number

    def close(self) -> None:
        self._callbacks.clear()
