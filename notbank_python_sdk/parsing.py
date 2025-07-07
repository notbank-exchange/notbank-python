from typing import Any, Callable, List, Type, TypeVar

from notbank_python_sdk.client_connection import ParseResponseFn, ParseResponseListFn
from notbank_python_sdk.core.either import Either
from notbank_python_sdk.core.converter import from_dict
from notbank_python_sdk.error import ErrorCode, NotbankException

T1 = TypeVar('T1')
T2 = TypeVar('T2')


def build_subscription_handler(
    handler: Callable[[T1], None],
    payload_parser: Callable[[str], Either[NotbankException, T1]]
) -> Callable[[Callable[[NotbankException], None]], Callable[[str], None]]:
    def subscription_handler_builder(
        on_failure: Callable[[NotbankException], None]
    ) -> Callable[[str], None]:
        def subscription_handler(payload_str: str) -> None:
            payload = payload_parser(payload_str)
            if payload.is_left():
                on_failure(payload.get_left())
                return
            try:
                handler(payload.get())
            except Exception as e:
                on_failure(NotbankException(ErrorCode.UNKNOWN, str(e)))
        return subscription_handler
    return subscription_handler_builder


def parse_response_fn(response_cls: Type[T2], no_pascal_case: List[str] = [], from_pascal_case: bool = True) -> ParseResponseFn[T2]:
    def parse_data_fn(data: Any) -> T2:
        return from_dict(response_cls, data, no_pascal_case, from_pascal_case)
    return parse_data_fn


def parse_response_list_fn(response_cls: Type[T2], no_pascal_case: List[str] = [], from_pascal_case: bool = True) -> ParseResponseListFn[T2]:
    def parse_data_fn(data: Any) -> List[T2]:
        return [from_dict(response_cls, elem, no_pascal_case, from_pascal_case) for elem in data]
    return parse_data_fn
