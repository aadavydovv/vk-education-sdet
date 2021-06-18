from _pytest.fixtures import FixtureRequest
from cases.base import CaseUIBase
from ui.pages.login import PageLogin
import allure
import pytest


class CaseUILogin(CaseUIBase):

    @pytest.fixture(scope='function', autouse=True)
    @allure.step('set up the "login ui" test case')
    def setup(self, driver, logger, request: FixtureRequest):
        self.setup_base(driver, logger)
        self.page_login: PageLogin = request.getfixturevalue('page_login')

        self.logger.info('completed the "login ui" test case setup')
