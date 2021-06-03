from faker import Faker
from mock.client import HTTPClient
import pytest


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, logger):
        self.client = HTTPClient(logger)

        self.faker_instance = Faker()
        self.name_first = self.faker_instance.first_name()
        self.name_last = self.faker_instance.last_name()

    @staticmethod
    def check_response(response, status, user_id=None, name_first=None, name_last=None, name_last_empty=False):
        message = response['message']

        if user_id:
            assert message['id'] == user_id

        if name_first:
            assert message['name_first'] == name_first

        if name_last:
            assert message['name_last'] == name_last

        if name_last_empty:
            assert not message.get('name_last')

        assert response['status'] == status
