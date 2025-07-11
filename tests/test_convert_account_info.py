
import simplejson as json
import unittest
from notbank_python_sdk.core import converter
from notbank_python_sdk.models.account_info import AccountInfo


class ConvertTickerFromJsonTestCase(unittest.TestCase):
    def test_ticker_from_list(self):
        account_info_json_str = "{\"OMSID\":1,\"AccountId\":235,\"AccountName\":\"Primary | ismael@dysopsis.com\",\"AccountHandle\":null,\"FirmId\":null,\"FirmName\":null,\"AccountType\":\"Asset\",\"FeeGroupId\":1,\"ParentID\":0,\"RiskType\":\"Normal\",\"MarginAccountStatus\":\"Active\",\"VerificationLevel\":0,\"VerificationLevelName\":null,\"CreditTier\":0,\"FeeProductType\":\"BaseProduct\",\"FeeProduct\":0,\"RefererId\":0,\"LoyaltyProductId\":0,\"LoyaltyEnabled\":false,\"PriceTier\":0,\"Frozen\":false,\"DateTimeUpdated\":\"2025-07-08T22:10:57.357Z\",\"DateTimeCreated\":\"2025-07-08T22:10:57.357Z\"}"
        account_info = converter.from_json_str(
            AccountInfo, account_info_json_str, overrides={"oms_id": "OMSID"})
        self.assertTrue(account_info.is_right())
