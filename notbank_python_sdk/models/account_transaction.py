from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class TransactionType(str, Enum):
    FEE = "Fee"
    TRADE = "Trade"
    OTHER = "Other"
    REVERSE = "Reverse"
    HOLD = "Hold"
    REBATE = "Rebate"
    MARGIN_ACQUISITION = "MarginAcquisition"
    MARGIN_RELINQUISH_BY_TRADE = "MarginRelinquishByTrade"
    MARGIN_INTEREST_TRANSFER = "MarginInterestTransfer"
    MARGIN_OPERATOR_TRANSFER_TO_MARGIN_ACCOUNT = "MarginOperatorTransferToMarginAccount"
    MARGIN_OPERATOR_TRANSFER_TO_ASSET_ACCOUNT = "MarginOperatorTransferToAssetAccount"
    MARGIN_USER_TRANSFER = "MarginUserTransfer"
    MARGIN_RELINQUISH_BY_TRANSFER = "MarginRelinquishByTransfer"
    MARGIN_RELINQUISH_BY_REVERSE_TRADE = "MarginRelinquishByReverseTrade"
    DISTRIBUTION = "Distribution"
    PAYMENT = "Payment"
    OPERATOR_LEND = "OperatorLend"
    OPERATOR_RECEIVED = "OperatorReceived"
    REBALANCE = "Rebalance"
    COMMISSION = "Commission"
    AIR_DROP = "AirDrop"


class TransactionReferenceType(str, Enum):
    TRADE = "Trade"
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"
    TRANSFER = "Transfer"
    ORDER_HOLD = "OrderHold"
    WITHDRAW_HOLD = "WithdrawHold"
    DEPOSIT_HOLD = "DepositHold"
    MARGIN_HOLD = "MarginHold"
    MANUAL_HOLD = "ManualHold"
    MANUAL_ENTRY = "ManualEntry"
    MARGIN_ACQUISITION = "MarginAcquisition"
    MARGIN_RELINQUISH = "MarginRelinquish"
    MARGIN_INTEREST_NETTING = "MarginInterestNetting"
    MARGIN_OPERATOR_TRANSFER_TO_MARGIN_ACCOUNT = "MarginOperatorTransferToMarginAccount"
    MARGIN_OPERATOR_TRANSFER_TO_ASSET_ACCOUNT = "MarginOperatorTransferToAssetAccount"
    MARGIN_USER_TRANSFER = "MarginUserTransfer"
    MARGIN_POSITION_REVERSE_TRADE = "MarginPositionReverseTrade"
    AFFILIATE_REBATE = "AffiliateRebate"
    DISTRIBUTION_ENTRY = "DistributionEntry"
    TRANSFER_HOLD = "TransferHold"
    AIR_DROP = "AirDrop"


@dataclass
class AccountTransaction:
    transaction_id: int
    reference_id: int
    oms_id: int
    account_id: int
    cr: Decimal  # Crédito
    dr: Decimal  # Débito
    counterparty: int
    transaction_type: TransactionType
    reference_type: TransactionReferenceType
    product_id: int
    time_stamp: int
    balance: Decimal = Decimal(0)
