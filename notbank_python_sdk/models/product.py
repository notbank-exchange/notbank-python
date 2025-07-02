from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    oms_id: int
    product_id: int
    product: str
    product_full_name: str
    master_data_unique_product_symbol: str
    product_type: str
    decimal_places: int
    tick_size: Decimal
    deposit_enabled: bool
    withdraw_enabled: bool
    no_fees: bool
    is_disabled: bool
    margin_enabled: bool
