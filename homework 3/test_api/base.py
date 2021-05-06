from api.client import ApiClient
import pytest


class ApiBase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config):
        self.api_client = ApiClient(config)

        self.api_client.post_auth()
        self.api_client.collect_csrftoken()
