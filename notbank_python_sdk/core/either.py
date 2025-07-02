from typing import Callable, Generic, Optional, TypeVar


L = TypeVar('L')
R = TypeVar('R')
L2 = TypeVar('L2')
R2 = TypeVar('R2')


class Either(Generic[L, R]):
    def __init__(self, left: Optional[L], right: Optional[R]):
        self._left = left
        self._right = right

    @staticmethod
    def right(right: R):
        return Either(None, right)

    @staticmethod
    def left(left: L):
        return Either(left, None)

    def is_right(self) -> bool:
        return self._right is not None

    def is_left(self) -> bool:
        return not self.is_right()

    def get(self) -> R:
        if self._right is None:
            raise ValueError("Cannot get right value from Either.Left")
        return self._right

    def get_left(self) -> L:
        if self._left is None:
            raise ValueError("Cannot get left value from Either.Right")
        return self._left

    def map(self, func: Callable[[R], R2]) -> 'Either[L, R2]':
        if self.is_right():
            return Either.Right(func(self._right))  # type: ignore
        return Either.left(self._left)  # type: ignore

    def map_left(self, func: Callable[[L], L2]) -> 'Either[L2, R]':
        if self.is_left():
            return Either.left(func(self._left))  # type: ignore
        return Either.Right(self._right)  # type: ignore

    def flat_map(self, func: Callable[[R], 'Either[L, R2]']) -> 'Either[L, R2]':
        if self.is_right():
            return func(self._right)  # type: ignore
        return Either.left(self._left)  # type: ignore

    def get_or_else(self, default: R) -> R:
        if self.is_right():
            return self._right  # type: ignore
        return default
