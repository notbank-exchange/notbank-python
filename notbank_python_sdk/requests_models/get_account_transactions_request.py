from dataclasses import dataclass
from enum import IntEnum
from typing import Optional, List
from notbank_python_sdk.models.account_transaction import TransactionReferenceType, TransactionType

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetAccountTransactionsRequest(WithOMSId):
    account_id: Optional[int] = None
    depth: Optional[int] = None
    product_id: Optional[int] = None
    transaction_id: Optional[int] = None
    reference_id: Optional[int] = None
    transaction_types: Optional[List[TransactionType]] = None
    transaction_reference_types: Optional[List[TransactionReferenceType]] = None
    start_timestamp: Optional[str] = None
    end_timestamp: Optional[str] = None
