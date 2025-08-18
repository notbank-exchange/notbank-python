from threading import Lock
from typing import Generic, TypeVar


T = TypeVar("T")


class SynchedValue(Generic[T]):
    _value: T
    _lock: Lock

    def __init__(self, value: T, lock: Lock):
        self._value = value
        self._lock = lock

    @staticmethod
    def create(value: T) -> 'SynchedValue[T]':
        return SynchedValue(value, Lock())

    def get(self) -> T:
        self._lock.acquire()
        value = self._value
        self._lock.release()
        return value

    def set(self, value: T) -> None:
        self._lock.acquire()
        self._value = value
        self._lock.release()
