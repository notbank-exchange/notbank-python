import unittest

from notbank_python_sdk.constants import ChileanCommune, Gender, IdentityType, Profession
from notbank_python_sdk.models.register_user_response import RegisterUserResponse
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import RegisterBasicUserRequest
from tests import test_helper


class TestRegisterBasicUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_register_basic_user(self):
        response = self.client.register_basic_user(RegisterBasicUserRequest(
            first_name="Juan",
            last_name="Perez",
            phone_number="+5511999999999",
            profession=Profession.TRADER,
            gender=Gender.MAN,
            birthdate="01/01/1990",
            citizenship="CL",
            identity_type=IdentityType.DNI,
            identity_number="26988728-1",
            identity_country="CL",
            address_country="CL",
            address_city="Santiago",
            address_street="Calle 1",
            address_postal_code="8320000",
            address_comune=ChileanCommune.SANTIAGO,
        ))
        self.assertIsNotNone(response)
        self.assertIsInstance(response, RegisterUserResponse)
        self.assertIsNotNone(response.user_id)
        self.assertIsNotNone(response.token)


if __name__ == "__main__":
    unittest.main()
