from decimal import Decimal
import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.models.fee_id import FeeId
from notbank_python_sdk.requests_models.set_oms_withdraw_fee import SetOmsWithdrawFeeRequest
from tests import test_helper

class TestSetOmsWithdrawFee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)


    def test_set_oms_withdraw_fee_success_example(self):
        # Create a request object matching the exact successful example provided
        req = SetOmsWithdrawFeeRequest(
            product_id=1,
            account_id=4,
            account_provider_id=2,
            fee_amt=Decimal(1.0),
            fee_calc_type=1,  # Using integer value from example
            is_active=True,
            minimal_fee_amt=Decimal(1),
            minimal_fee_calc_type=1  # Using integer value from example
        )
        # Call the client method
        res = self.client.set_oms_withdraw_fee(req)

        # Assert that the response is not None and matches the expected success response structure and value
        self.assertIsNotNone(res)
        self.assertIsInstance(res, FeeId)
        self.assertEqual(res.fee_id, 1)

    def test_set_oms_withdraw_fee_with_defaults(self):
        # Test with only required fields to see how the mock handles it
        # Based on the mock logic, this will NOT match the exact success example
        # and the mock will return None. The SystemClient will then return None.
        # This tests that sending a request with defaults doesn't raise an immediate error
        # within the request object itself or the client call setup.
        req = SetOmsWithdrawFeeRequest(
            product_id=99  # Different ProductId
            # All other fields use defaults (0, 0.0, False, "Internal", None etc.)
        )
        res = self.client.set_oms_withdraw_fee(req)

        # Assert that the response is None, as the mock is designed to return None for non-example inputs
        self.assertIsNone(res)

    # Note: We cannot reliably test other specific error conditions (like Invalid Request, etc.)
    # with the current SetOmsWithdrawFeeResponse model as it only defines the success structure (fee_id).
    # A full test suite would require a response model or error handling mechanism that
    # can parse the API's actual error responses.


if __name__ == "__main__":
    unittest.main()
