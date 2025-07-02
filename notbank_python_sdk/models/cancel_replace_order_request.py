from dataclasses import dataclass


@dataclass
class CancelReplaceOrderResponse:
    replacement_order_id: int
    replacement_cl_ord_id: int
    orig_order_id: int
    orig_cl_ord_id: int
