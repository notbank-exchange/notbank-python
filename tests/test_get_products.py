import unittest
from notbank_python_sdk.notbank_client import NotbankClient

from notbank_python_sdk.requests_models.get_products_request import GetProductsRequest
from tests import test_helper


class TestGetProducts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection()
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_get_products_success(self):
        """
        Prueba exitosa: obtiene una lista de productos válidos.
        """
        products = self.client.get_products()

        # Verificamos que la respuesta contiene dos productos
        self.assertEqual(len(products), 2)

        # Verificamos los detalles del primer producto
        self.assertEqual(products[0].product, "USD")
        self.assertEqual(products[0].product_type, "NationalCurrency")
        self.assertEqual(products[0].decimal_places, 2)
        self.assertEqual(products[0].tick_size, 0.01)
        self.assertEqual(products[0].deposit_enabled, True)
        self.assertEqual(products[0].withdraw_enabled, True)
        self.assertEqual(products[0].no_fees, False)
        self.assertEqual(products[0].is_disabled, False)
        self.assertEqual(products[0].margin_enabled, False)

        # Verificamos los detalles del segundo producto
        self.assertEqual(products[1].product, "BTC")
        self.assertEqual(products[1].product_type, "CryptoCurrency")
        self.assertEqual(products[1].decimal_places, 8)
        self.assertEqual(products[1].tick_size, 0.00000001)
        self.assertEqual(products[1].deposit_enabled, True)
        self.assertEqual(products[1].withdraw_enabled, True)
        self.assertEqual(products[1].no_fees, False)
        self.assertEqual(products[1].is_disabled, False)
        self.assertEqual(products[1].margin_enabled, False)

if __name__ == "__main__":
    unittest.main()
