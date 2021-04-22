from selenium.common.exceptions import TimeoutException
from ui.locators import LocatorsAuth
from ui.pages.base import PageBase
from ui.pages.post_auth import PagePostAuth
import allure
import pytest


class PageAuth(PageBase):
    locators = LocatorsAuth()

    @pytest.mark.UI
    @allure.step('logging in')
    def log_in(self, config, login=None, password=None):
        self.click(self.locators.BUTTON_LOG_IN_MENU)

        self.input(self.locators.INPUT_LOGIN, login if login else config['login'])
        self.input(self.locators.INPUT_PASSWORD, password if password else config['password'])

        self.click(self.locators.BUTTON_LOG_IN)

    @allure.step('checking if authorization failed using locator')
    def check_failed_auth_by_locator(self):
        with pytest.raises(TimeoutException):
            self.find(PagePostAuth.locators.BUTTON_SEGMENTS)

    @allure.step('checking if authorization failed using url')
    def check_failed_auth_by_url(self):
        with pytest.raises(AssertionError):
            assert self.driver.current_url == PagePostAuth.url
