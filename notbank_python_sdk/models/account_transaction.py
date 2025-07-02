from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class TransactionType(str, Enum):
    fee = "Fee"
    trade = "Trade"
    other = "Other"
    reverse = "Reverse"
    hold = "Hold"
    rebate = "Rebate"
    margin_acquisition = "MarginAcquisition"
    margin_relinquish_by_trade = "MarginRelinquishByTrade"
    margin_interest_transfer = "MarginInterestTransfer"
    margin_operator_transfer_to_margin_account = "MarginOperatorTransferToMarginAccount"
    margin_operator_transfer_to_asset_account = "MarginOperatorTransferToAssetAccount"
    margin_user_transfer = "MarginUserTransfer"
    margin_relinquish_by_transfer = "MarginRelinquishByTransfer"
    margin_relinquish_by_reverse_trade = "MarginRelinquishByReverseTrade"
    distribution = "Distribution"
    payment = "Payment"
    operator_lend = "OperatorLend"
    operator_received = "OperatorReceived"
    rebalance = "Rebalance"
    commission = "Commission"
    air_drop = "AirDrop"


class TransactionReferenceType(str, Enum):
    trade = "Trade"
    deposit = "Deposit"
    withdraw = "Withdraw"
    transfer = "Transfer"
    order_hold = "OrderHold"
    withdraw_hold = "WithdrawHold"
    deposit_hold = "DepositHold"
    margin_hold = "MarginHold"
    manual_hold = "ManualHold"
    manual_entry = "ManualEntry"
    margin_acquisition = "MarginAcquisition"
    margin_relinquish = "MarginRelinquish"
    margin_interest_netting = "MarginInterestNetting"
    margin_operator_transfer_to_margin_account = "MarginOperatorTransferToMarginAccount"
    margin_operator_transfer_to_asset_account = "MarginOperatorTransferToAssetAccount"
    margin_user_transfer = "MarginUserTransfer"
    margin_position_reverse_trade = "MarginPositionReverseTrade"
    affiliate_rebate = "AffiliateRebate"
    distribution_entry = "DistributionEntry"
    transfer_hold = "TransferHold"
    air_drop = "AirDrop"


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
