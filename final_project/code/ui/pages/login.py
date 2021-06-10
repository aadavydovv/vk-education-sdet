from misc.constants import MYAPP_PORT
from selenium.common.exceptions import TimeoutException
from ui.locators import LocatorsLogin
from ui.pages.authorization import PageAuthorization
from ui.pages.home import PageHome
from ui.pages.registration import PageRegistration
import allure


class PageLogin(PageAuthorization):

    url = f'http://myapp:{MYAPP_PORT}/login'
    locators = LocatorsLogin()

    @allure.step('log in using username {username} and password {password}')
    def log_in(self, username, password):
        self.input(self.locators.INPUT_USERNAME, username)
        self.input(self.locators.INPUT_PASSWORD, password)
        self.click(self.locators.BUTTON_SUBMIT)

        try:
            self.find(self.locators.INPUT_USERNAME, timeout=2)
        except TimeoutException:
            self.logger.info(f'logged in as "{username}" with password "{password}"')
            return PageHome(self.driver, self.logger)

    @allure.step('visit the registration page')
    def visit_registration_page(self):
        self.click(self.locators.LINK_CREATE_ACCOUNT)
        self.logger.info('visiting the registration page')
        return PageRegistration(self.driver, self.logger)
