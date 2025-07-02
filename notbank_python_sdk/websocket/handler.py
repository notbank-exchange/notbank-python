from typing import Any, Callable


class WebsocketHandler:
    def __init__(
        self,
        handle: Callable[[Any], None],
        on_open: Callable[[], None] = lambda: None,
        on_close: Callable[[Any, str], None] = lambda code, message: None,
        on_failure: Callable[[Exception], None] = lambda e: None,
    ) -> None:
        self._handle = handle
        self._on_open = on_open
        self._on_close = on_close
        self._on_failure = on_failure

    def handle(self, data: Any) -> None:
        self._handle(data)

    def on_open(self) -> None:
        self._on_open()

    def on_close(self, code: int, message: str) -> None:
        self._on_close(code, message)

    def on_error(self, error: Exception) -> None:
        self._on_failure(error)
