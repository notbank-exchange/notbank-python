from dataclasses import dataclass
from decimal import Decimal
from typing import List


@dataclass
class Level2TickerSnapshot:
    md_update_id: int
    number_of_unique_accounts: int
    action_date_time: int
    action_type: int
    last_trade_price: Decimal
    number_of_orders: int
    price: Decimal
    product_pair_code: int
    quantity: Decimal
    side: int
