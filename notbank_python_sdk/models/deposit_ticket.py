from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional
from enum import IntEnum


class DepositTicketStatus(IntEnum):
    new = 0
    admin_processing = 1
    accepted = 2
    rejected = 3
    system_processing = 4
    fully_processed = 5
    failed = 6
    pending = 7
    confirmed = 8
    aml_processing = 9
    aml_accepted = 10
    aml_rejected = 11
    aml_failed = 12
    limits_accepted = 13
    limits_rejected = 14


@dataclass
class Comment:
    comment_id: int
    entered_by: int
    entered_date_time: str
    entered_date_time_tick: int
    comment: str
    operator_id: int
    oms_id: int
    ticket_id: int


@dataclass
class DepositTicket:
    asset_manager_id: Optional[int] = None
    account_provider_id: Optional[int] = None
    account_id: Optional[int] = None
    asset_id: Optional[int] = None
    account_name: Optional[str] = None
    asset_name: Optional[str] = None
    amount: Optional[Decimal] = None
    notional_value: Optional[Decimal] = None
    notional_product_id: Optional[int] = None
    oms_id: Optional[int] = None
    request_code: Optional[str] = None
    reference_id: Optional[str] = None
    request_ip: Optional[str] = None
    request_user: Optional[int] = None
    request_user_name: Optional[str] = None
    operator_id: Optional[int] = None
    status: Optional[DepositTicketStatus] = None
    fee_amt: Optional[Decimal] = None
    updated_by_user: Optional[int] = None
    updated_by_user_name: Optional[str] = None
    ticket_number: Optional[int] = None
    deposit_info: Optional[str] = None
    reject_reason: Optional[str] = None
    created_timestamp: Optional[str] = None
    last_update_time_stamp: Optional[str] = None
    created_timestamp_tick: Optional[int] = None
    last_update_timestamp_tick: Optional[int] = None
    comments: Optional[List[Comment]] = None
    attachments: Optional[List[str]] = None
    from_address: Optional[str] = None
