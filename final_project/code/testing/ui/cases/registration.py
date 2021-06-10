from _pytest.fixtures import FixtureRequest
from cases.base import CaseUIBase
from ui.pages.login import PageLogin
import allure
import pytest


class CaseUIRegistration(CaseUIBase):

    @pytest.fixture(scope='function', autouse=True)
    @allure.step('set up the "registration ui" test case')
    def setup(self, driver, logger, request: FixtureRequest):
        self.setup_base(driver, logger)

        page_login: PageLogin = request.getfixturevalue('page_login')
        self.page_registration = page_login.visit_registration_page()

        self.logger.info('completed the "registration ui" test case setup')
