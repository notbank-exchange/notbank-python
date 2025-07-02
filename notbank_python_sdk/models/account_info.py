from dataclasses import dataclass
from typing import Optional


@dataclass
class AccountInfo:
    oms_id: int
    account_id: int
    account_name: str
    risk_type: str
    account_type: str
    fee_product_type: str
    account_handle: Optional[str] = None
    firm_id: Optional[int] = None
    firm_name: Optional[str] = None
    fee_group_id: Optional[int] = None
    parent_id: Optional[int] = None
    verification_level: Optional[int] = None
    verification_level_name: Optional[str] = None
    credit_tier: Optional[int] = None
    fee_product: Optional[int] = None
    referer_id: Optional[int] = None
    loyalty_product_id: Optional[int] = None
    loyalty_enabled: Optional[bool] = None
    price_tier: Optional[int] = None
    frozen: Optional[bool] = None
