from faker import Faker
from mock.client import HTTPClient
import pytest


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, logger):
        self.client = HTTPClient(logger)

        faker_instance = Faker()
        self.name_first = faker_instance.first_name()
        self.name_last = faker_instance.last_name()
