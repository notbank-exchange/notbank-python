import unittest

from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_product_request import GetProductRequest
from tests import test_helper


class TestGetProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_product_success(self):
        """
        Prueba exitosa: solicitud válida, devuelve los detalles del producto.
        """
        request = GetProductRequest(product_id=1)
        response = self.client.get_product(request)

        # Verificaciones
        self.assertIsNotNone(response)
        self.assertEqual(response.oms_id, 1)
        self.assertEqual(response.product_id, 1)
        self.assertEqual(response.product, "USD")
        self.assertEqual(response.product_full_name, "US Dollar")
        self.assertEqual(response.product_type, "NationalCurrency")
        self.assertEqual(response.decimal_places, 2)
        self.assertEqual(response.tick_size, 0.01)
        self.assertEqual(response.deposit_enabled, True)
        self.assertEqual(response.withdraw_enabled, True)
        self.assertEqual(response.no_fees, False)
        self.assertEqual(response.is_disabled, False)
        self.assertEqual(response.margin_enabled, False)

    def test_get_product_not_found(self):
        """
        Prueba: product_id inválido, no se encuentra el producto.
        """
        request = GetProductRequest(
            product_id=999,  # product_id inválido
        )
        response = self.client.get_product(request)

        # Verificaciones
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
