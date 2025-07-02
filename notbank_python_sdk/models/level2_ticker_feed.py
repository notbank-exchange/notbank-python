from decimal import Decimal
from typing import Any, List
from notbank_python_sdk.core.either import Either

from notbank_python_sdk.error import ErrorCode, NotbankException
from dataclasses import dataclass

import simplejson as json


@dataclass
class Level2TickerFeed:
    market_data_update_id: int
    number_of_accounts: int
    action_date_time: int
    action_type: int
    last_trade_price: Decimal
    number_of_orders: int
    price: Decimal
    product_pair_code: int
    quantity: Decimal
    side: int


def level2_ticker_feed_from_list(json_list: List[Any]) -> Level2TickerFeed:
    return Level2TickerFeed(
        market_data_update_id=json_list[0],
        number_of_accounts=json_list[1],
        action_date_time=json_list[2],
        action_type=json_list[3],
        last_trade_price=Decimal(json_list[4]),
        number_of_orders=json_list[5],
        price=Decimal(json_list[6]),
        product_pair_code=json_list[7],
        quantity=Decimal(json_list[8]),
        side=json_list[9]
    )


def level_2_ticker_feed_list_from_json_str(json_str: str) -> Either[NotbankException, List[Level2TickerFeed]]:
    try:
        json_list = json.loads(json_str, use_decimal=True)
        return Either.right([level2_ticker_feed_from_list(item) for item in json_list])
    except Exception as e:
        return Either.left(NotbankException(ErrorCode.CONFIGURATION_ERROR, str(e)))
