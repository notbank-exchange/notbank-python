from decimal import Decimal
import unittest

from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models.fee_request import FeeRequest

from tests import test_helper


class TestGetWithdrawFee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_withdraw_fee_success(self):
        """
        Prueba exitosa: solicitud válida, devuelve el fee estimado.
        """
        request = FeeRequest(
            account_id=1,
            product_id=1,
            amount=Decimal(100),
            account_provider_id=3,  # Opcional
        )
        response = self.client.get_withdraw_fee(request)

        # Verificaciones
        self.assertIsNotNone(response)
        self.assertEqual(response.fee_amount, 1.0)
        self.assertEqual(response.ticket_amount, 100)

    def test_get_withdraw_fee_default(self):
        """
        Prueba: solicitud con valores predeterminados, devuelve el fee estimado.
        """
        request = FeeRequest(
            account_id=1,
            product_id=1,
            amount=Decimal(50),
            account_provider_id=0,  # Valor predeterminado
        )
        response = self.client.get_withdraw_fee(request)

        # Verificaciones
        self.assertIsNotNone(response)
        self.assertEqual(response.fee_amount, 0.5)
        self.assertEqual(response.ticket_amount, 50)


if __name__ == "__main__":
    unittest.main()
