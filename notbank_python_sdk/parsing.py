from typing import Any, Callable, Dict, List, Optional, Type, TypeVar

from notbank_python_sdk.client_connection import ParseResponseFn, ParseResponseListFn
from notbank_python_sdk.core.either import Either
from notbank_python_sdk.core.converter import from_dict
from notbank_python_sdk.error import ErrorCode, NotbankException, StandardErrorResponse

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


def parse_response_fn(response_cls: Type[T2], no_pascal_case: List[str] = [], overrides: Dict[str, str] = {}, from_pascal_case: bool = True) -> ParseResponseFn[T2]:
    def parse_data_fn(data: Any) -> T2:
        return from_dict(response_cls, data, no_pascal_case, overrides, from_pascal_case)
    return parse_data_fn


def parse_report_response_fn(response_cls: Type[T2], no_pascal_case: List[str] = [], overrides: Dict[str, str] = {}, from_pascal_case: bool = True) -> ParseResponseFn[T2]:
    def parse_data_fn(data: Any) -> T2:
        error = get_report_error(data)
        if error is not None and error.result is False:
            raise NotbankException.create(error)
        return from_dict(response_cls, data, no_pascal_case, overrides, from_pascal_case)
    return parse_data_fn


def get_report_error(data: Any) -> Optional[StandardErrorResponse]:
    try:
        error = from_dict(StandardErrorResponse, data, [], overrides={
                          "result": "bAccepted",  "errormsg": "rejectMessage", "detail": "requestId"})
        error.errorcode = ErrorCode.UNKNOWN
        if error.detail is not None:
            error.detail = "request id: " + error.detail
        return error
    except Exception as e:
        return None


def parse_response_list_fn(response_cls: Type[T2], no_pascal_case: List[str] = [], overrides: Dict[str, str] = {}, from_pascal_case: bool = True) -> ParseResponseListFn[T2]:
    def parse_data_fn(data: Any) -> List[T2]:
        return [from_dict(response_cls, elem, no_pascal_case, overrides, from_pascal_case) for elem in data]
    return parse_data_fn
