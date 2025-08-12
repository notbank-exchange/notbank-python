from typing import Any, Callable, NamedTuple, Optional


class ConnectionConfiguration(NamedTuple):
    uri: str
    on_open: Callable[[], None] = lambda: None
    on_close: Callable[[Any, str], None] = lambda code, message: None
    on_failure: Callable[[Exception], None] = lambda e: None
    peek_message_in: Callable[[str], None] = lambda x: None
    peek_message_out: Callable[[str], None] = lambda x: None
    request_timeout: Optional[float] = None
