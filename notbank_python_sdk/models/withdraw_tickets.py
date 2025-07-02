from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class WithdrawTicket:
    oms_id: int
    account_id: int
    asset_manager_id: Optional[int] = None
    account_provider_id: Optional[int] = None
    account_name: Optional[str] = None
    asset_id: Optional[int] = None
    asset_name: Optional[str] = None
    amount: Optional[Decimal] = None
    notional_value: Optional[Decimal] = None
    notional_product_id: Optional[int] = None
    template_form: Optional[str] = None
    template_form_type: Optional[str] = None
    request_code: Optional[str] = None
    request_ip: Optional[str] = None
    request_user_id: Optional[int] = None
    request_user_name: Optional[str] = None
    operator_id: Optional[int] = None
    status: Optional[int] = None
    fee_amt: Optional[Decimal] = None
    updated_by_user: Optional[int] = None
    updated_by_user_name: Optional[str] = None
    ticket_number: Optional[int] = None
    withdraw_transaction_details: Optional[str] = None
    reject_reason: Optional[str] = None
    created_time_stamp: Optional[str] = None
    last_update_time_stamp: Optional[str] = None
    created_timestamp_tick: Optional[int] = None
    last_update_timestamp_tick: Optional[int] = None
    comments: List[str] = field(default_factory=list)
    attachments: List[str] = field(default_factory=list)
    audit_log: List[str] = field(default_factory=list)
