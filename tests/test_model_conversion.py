from decimal import Decimal
from unittest import TestCase, main

from notbank_python_sdk.models.oms_fee import OmsFee
from notbank_python_sdk.requests_models.account_fees_request import AccountFeesRequest
from notbank_python_sdk.core.converter import from_dict, from_json_str, to_dict
from notbank_python_sdk.websocket.message_frame import MessageFrame


class ModelConversionTestCase(TestCase):
    def test_oms_id_to_dict(self):
        account_fee_request = AccountFeesRequest(account_id=9)
        data = to_dict(account_fee_request)
        self.assertEqual(data["OMSId"], account_fee_request.oms_id)
        self.assertEqual(data["AccountId"], account_fee_request.account_id)

    def test_from_dict(self):
        data = {
            "OMSId": 111,
            "AccountId": 222,
            "AccountProviderId": 333,
            "FeeId": 444,
            "FeeAmt": 5.55,
            "FeeCalcType": "aType",
            "IsActive": True,
            "ProductId": 666,
            "MinimalFeeAmt": 7.77,
            "MinimalFeeCalcType": "anotherType"
        }
        deposit_fee = from_dict(OmsFee, data)

        self.assertEqual(deposit_fee.fee_amt, Decimal('5.55'))
        self.assertEqual(deposit_fee.oms_id, 111)

    def test_to_dict(self):
        deposit_fee = OmsFee(
            oms_id=111,
            account_id=222,
            account_provider_id=333,
            fee_id=444,
            fee_amt=Decimal('5.55'),
            fee_calc_type='aType',
            is_active=True,
            product_id=666,
            minimal_fee_amt=Decimal('7.77'),
            minimal_fee_calc_type="anotherType"
        )
        data = to_dict(deposit_fee)
        self.assertEqual(data['OMSId'], deposit_fee.oms_id)
        self.assertEqual(data['FeeAmt'], str(deposit_fee.fee_amt))

    def test_json_str_to_message_frame(self):
        json_str = '{"m":1, "i":2, "n":"SubscribeLevel1", "o":"{ \\"OMSId\\":1 }"}'
        message_frame = from_json_str(MessageFrame, json_str)
        self.assertTrue(message_frame.is_right(),
                        lambda: message_frame.get_left())


if __name__ == '__main__':
    main()
