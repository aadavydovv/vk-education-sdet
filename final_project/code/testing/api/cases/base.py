from myapp_api.client import APIClient
import allure
import pytest


class UnexpectedResponseStatusException(Exception):
    pass


class CaseAPIBase:

    @pytest.fixture(scope='function', autouse=True)
    @allure.step('setup the "base api" test case')
    def setup(self, logger):
        self.api_client = APIClient(logger)
        self.logger = logger

        self.logger.info('completed the "base api" test case setup')

    @staticmethod
    @allure.step('check the response status - {expected_status} is expected')
    def check_response_status(response, expected_status):
        if response.status_code != expected_status:
            raise UnexpectedResponseStatusException(f'got {response.status_code} {response.reason} '
                                                    f'for url "{response.url}"\n'
                                                    f'expected status code: {expected_status}')
