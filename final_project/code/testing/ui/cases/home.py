from _pytest.fixtures import FixtureRequest
from cases.base import CaseUIBase
from misc.constants import CONTROL_USER_USERNAME, CONTROL_USER_PASSWORD
from ui.pages.home import PageHome
from ui.pages.login import PageLogin
import allure
import pytest


class CaseUIHome(CaseUIBase):

    @pytest.fixture(scope='function', autouse=True)
    @allure.step('setup the "home ui" test case')
    def setup(self, driver, logger, request: FixtureRequest):
        self.setup_base(driver, logger)

        page_login: PageLogin = request.getfixturevalue('page_login')
        self.page_login_url = page_login.url
        self.page_home: PageHome = page_login.log_in(CONTROL_USER_USERNAME, CONTROL_USER_PASSWORD)

        self.logger.info('completed the "home ui" test case setup')

    @allure.step('check if the current url differs from the target url ({target_url})')
    def check_url(self, target_url):
        current_url = self.driver.current_url
        assert current_url == target_url, f'the driver\'s current url ({current_url}) ' \
                                          f'differs from the target url ({target_url})'

    @allure.step('switch to the last opened tab')
    def switch_to_last_opened_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.logger.info('switched to the last opened tab')
