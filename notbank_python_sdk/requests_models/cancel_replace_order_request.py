from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Union

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class CancelReplaceOrderRequest(WithOMSId):
    order_id_to_replace: int
    client_order_id: Optional[int] = None
    order_type: Optional[Union[int, str]] = None
    side: Optional[Union[int, str]] = None
    account_id: Optional[int] = None
    instrument_id: Optional[int] = None
    use_display_quantity: Optional[bool] = False
    display_quantity: Optional[Decimal] = None
    limit_price: Optional[Decimal] = None
    stop_price: Optional[Decimal] = None
    reference_price: Optional[Decimal] = None
    peg_price_type: Optional[Union[int, str]] = None
    time_in_force: Optional[Union[int, str]] = None
    order_id_oco: Optional[int] = None
    quantity: Optional[Decimal] = None
