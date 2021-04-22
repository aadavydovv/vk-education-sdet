import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.auth import PageAuth


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.page_auth: PageAuth = request.getfixturevalue('page_auth')

        self.logger.debug('setup is complete')
