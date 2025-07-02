from dataclasses import dataclass
from decimal import Decimal
import simplejson as json
from typing import Any, List
from notbank_python_sdk.core.either import Either

from notbank_python_sdk.error import ErrorCode, NotbankException


@dataclass
class PublicTrade:
    trade_id: int
    instrument_id: int
    quantity: Decimal
    price: Decimal
    order1: int
    order2: int
    trade_time: int
    direction: int
    taker_side: int
    block_trade: bool
    order_client_id: int


def public_trade_from_list(list_str: List[Any]) -> PublicTrade:
    return PublicTrade(
        trade_id=list_str[0],
        instrument_id=list_str[1],
        quantity=list_str[2],
        price=list_str[3],
        order1=list_str[4],
        order2=list_str[5],
        trade_time=list_str[6],
        direction=list_str[7],
        taker_side=list_str[8],
        block_trade=list_str[9] == 1,
        order_client_id=list_str[10]
    )


def public_trade_list_from_json_str(json_str: str) -> Either[NotbankException, List[PublicTrade]]:
    try:
        json_list = json.loads(json_str, use_decimal=True)
        return Either.right([public_trade_from_list(item) for item in json_list])
    except Exception as e:
        return Either.left(NotbankException(ErrorCode.CONFIGURATION_ERROR, str(e)))
