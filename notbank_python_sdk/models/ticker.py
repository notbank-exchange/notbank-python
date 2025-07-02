from dataclasses import dataclass
from decimal import Decimal

import simplejson as json
from typing import Any, List
from notbank_python_sdk.core.either import Either

from notbank_python_sdk.error import ErrorCode, NotbankException


@dataclass
class Ticker:
    end_date_time: int
    high: Decimal
    low: Decimal
    open: Decimal
    close: Decimal
    volume: Decimal
    bid: Decimal
    ask: Decimal
    instrument_id: int
    begin_date_time: int


def ticker_from_list(json_list: List[Any]) -> Ticker:
    return Ticker(
        end_date_time=json_list[0],
        high=Decimal(json_list[1]),
        low=Decimal(json_list[2]),
        open=Decimal(json_list[3]),
        close=Decimal(json_list[4]),
        volume=Decimal(json_list[5]),
        bid=Decimal(json_list[6]),
        ask=Decimal(json_list[7]),
        instrument_id=json_list[8],
        begin_date_time=json_list[9],
    )


def ticker_list_from_json_str(json_str: str) -> Either[NotbankException, List[Ticker]]:
    try:
        json_list = json.loads(json_str, use_decimal=True)
        return Either.right([ticker_from_list(item) for item in json_list])
    except Exception as e:
        return Either.left(NotbankException(ErrorCode.CONFIGURATION_ERROR, str(e)))
