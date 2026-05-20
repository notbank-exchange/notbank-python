import unittest

from notbank_python_sdk.constants import Gender, IdentityType, Profession
from notbank_python_sdk.models.register_user_response import RegisterUserResponse
from notbank_python_sdk.notbank_client import NotbankClient
from notbank_python_sdk.requests_models import RegisterAdvancedUserRequest
from tests import test_helper


class TestRegisterAdvancedUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = test_helper.new_rest_client_connection(
            test_helper.print_message_in, test_helper.print_message_out)
        cls.credentials = test_helper.load_credentials()
        test_helper.authenticate_connection(connection, cls.credentials)
        cls.client = NotbankClient(connection)

    def test_register_advanced_user(self):
        response = self.client.register_advanced_user(RegisterAdvancedUserRequest(
            first_name="Juan",
            last_name="Perez",
            phone_number="+56911111111",
            profession=Profession.TRADER,
            gender=Gender.MAN,
            birthdate="01/01/1990",
            citizenship="CL",
            identity_type=IdentityType.PASAPORTE,
            identity_number="P12345678",
            identity_country="CL",
            address_country="CL",
            address_city="Santiago",
            address_street="Calle 1",
            address_postal_code="8320000",
            pep=False,
            subject_comply=False,
            is_public_servant=False,
        ))
        self.assertIsNotNone(response)
        self.assertIsInstance(response, RegisterUserResponse)
        self.assertIsNotNone(response.user_id)
        self.assertIsNotNone(response.token)


if __name__ == "__main__":
    unittest.main()
