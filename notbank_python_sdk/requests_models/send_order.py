from dataclasses import dataclass
from decimal import Decimal
from enum import IntEnum
from typing import Optional

from notbank_python_sdk.core.tools import truncate_dec
from notbank_python_sdk.models.instrument import Instrument
from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


class TimeInForce(IntEnum):
    GTC = 1
    OPG = 2
    IOC = 3
    FOK = 4
    GTX = 5
    GTD = 6


class Side(IntEnum):
    Buy = 0
    Sell = 1


class OrderType(IntEnum):
    Market = 1
    Limit = 2
    StopMarket = 3
    StopLimit = 4
    TrailingStopMarket = 5
    TrailingStopLimit = 6
    BlockTrade = 7


class PegPriceType(IntEnum):
    Last = 1
    Bid = 2
    Ask = 3


@dataclass
class SendOrderRequest(WithOMSId):
    instrument: Instrument
    account_id: int
    time_in_force: TimeInForce
    side: Side
    order_type: OrderType
    quantity: Decimal
    client_order_id: Optional[int] = None
    order_id_oco: Optional[int] = None
    use_display_quantity: Optional[bool] = None
    peg_price_type: Optional[PegPriceType] = None
    limit_price: Optional[Decimal] = None
    stop_price: Optional[Decimal] = None
    trailing_amount: Optional[Decimal] = None
    limit_offset: Optional[Decimal] = None
    display_quantity: Optional[int] = None
    value: Optional[Decimal] = None


@dataclass
class SendOrderRequestInternal:
    oms_id: int
    instrument_id: int
    account_id: int
    time_in_force: int
    side: int
    order_type: int
    quantity: Decimal
    client_order_id: Optional[int] = None
    order_id_oco: Optional[int] = None
    use_display_quantity: Optional[bool] = None
    peg_price_type: Optional[int] = None
    limit_price: Optional[Decimal] = None
    stop_price: Optional[Decimal] = None
    trailing_amount: Optional[Decimal] = None
    limit_offset: Optional[Decimal] = None
    display_quantity: Optional[int] = None
    value: Optional[Decimal] = None

    @staticmethod
    def from_send_order_request(order_request: SendOrderRequest) -> 'SendOrderRequestInternal':
        instrument = order_request.instrument

        quantity = truncate_dec(order_request.quantity,
                                instrument.quantity_increment)

        stop_price = order_request.stop_price
        if stop_price is not None:
            stop_price = truncate_dec(stop_price, instrument.price_increment)

        limit_price = order_request.limit_price
        if limit_price is not None:
            limit_price = truncate_dec(limit_price, instrument.price_increment)

        return SendOrderRequestInternal(
            oms_id=order_request.oms_id,
            instrument_id=instrument.instrument_id,
            account_id=order_request.account_id,
            time_in_force=int(order_request.time_in_force),
            side=int(order_request.side),
            order_type=int(order_request.order_type),
            client_order_id=order_request.client_order_id,
            order_id_oco=order_request.order_id_oco,
            use_display_quantity=order_request.use_display_quantity,
            quantity=quantity,
            peg_price_type=int(
                order_request.peg_price_type) if order_request.peg_price_type is not None else None,
            limit_price=limit_price,
            stop_price=stop_price,
            trailing_amount=order_request.trailing_amount,
            limit_offset=order_request.limit_offset,
            display_quantity=order_request.display_quantity,
            value=order_request.value,
        )
