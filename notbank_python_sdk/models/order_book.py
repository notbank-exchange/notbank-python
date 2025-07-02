from dataclasses import dataclass
from decimal import Decimal
from typing import List


@dataclass
class OrderBookLevel:
    quantity: Decimal
    price: Decimal


@dataclass
class OrderBook:
    timestamp: int
    bids: List[OrderBookLevel]
    asks: List[OrderBookLevel]


@dataclass
class OrderBookRaw:
    timestamp: int
    bids: List[List[Decimal]]
    asks: List[List[Decimal]]


def order_book_from_raw(raw: OrderBookRaw) -> OrderBook:
    bids = [
        OrderBookLevel(quantity=Decimal(level[0]), price=Decimal(level[1]))
        for level in raw.bids]
    asks = [
        OrderBookLevel(quantity=Decimal(level[0]), price=Decimal(level[1]))
        for level in raw.asks]
    return OrderBook(timestamp=raw.timestamp, bids=bids, asks=asks)
