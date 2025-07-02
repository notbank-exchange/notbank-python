from dataclasses import dataclass
from enum import IntEnum
from typing import Optional, List

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


class TransactionTypes(IntEnum):
    FEE = 1
    TRADE = 2
    OTHER = 3
    REVERSE = 4
    HOLD = 5
    REBATE = 6
    MARGIN_ACQUISITION = 7
    MARGIN_RELINQUISH_BY_TRADE = 8
    MARGIN_INTEREST_TRANSFER = 9
    MARGIN_OPERATOR_TRANSFER_TO_MARGIN_ACCOUNT = 10
    MARGIN_OPERATOR_TRANSFER_TO_ASSET_ACCOUNT = 11
    MARGIN_USER_TRANSFER = 12
    MARGIN_RELINQUISH_BY_TRANSFER = 13
    MARGIN_RELINQUISH_BY_REVERSE_TRADE = 14
    DISTRIBUTION = 15
    PAYMENT = 16
    OPERATOR_LEND = 21
    OPERATOR_RECEIVED = 22
    REBALANCE = 23
    COMMISSION = 24
    AIR_DROP = 25


class TransactionReferenceTypes(IntEnum):
    TRADE = 1
    DEPOSIT = 2
    WITHDRAW = 3
    TRANSFER = 4
    ORDER_HOLD = 5
    WITHDRAW_HOLD = 6
    DEPOSIT_HOLD = 7
    MARGIN_HOLD = 8
    MANUAL_HOLD = 9
    MANUAL_ENTRY = 10
    MARGIN_ACQUISITION = 11
    MARGIN_RELINQUISH = 12
    MARGIN_INTEREST_NETTING = 13
    MARGIN_OPERATOR_TRANSFER_TO_MARGIN_ACCOUNT = 14
    MARGIN_OPERATOR_TRANSFER_TO_ASSET_ACCOUNT = 15
    MARGIN_USER_TRANSFER = 16
    MARGIN_POSITION_REVERSE_TRADE = 17
    AFFILIATE_REBATE = 18
    DISTRIBUTION_ENTRY = 19
    TRANSFER_HOLD = 20
    AIR_DROP = 21


@dataclass
class GetAccountTransactionsRequest(WithOMSId):
    account_id: Optional[int] = None
    depth: Optional[int] = None
    product_id: Optional[int] = None
    transaction_id: Optional[int] = None
    reference_id: Optional[int] = None
    transaction_types: Optional[List[TransactionTypes]] = None
    transaction_reference_types: Optional[List[TransactionReferenceTypes]] = None
    start_timestamp: Optional[str] = None
    end_timestamp: Optional[str] = None
