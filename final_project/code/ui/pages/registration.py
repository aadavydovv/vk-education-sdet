from misc.constants import MYAPP_PORT
from selenium.common.exceptions import TimeoutException
from ui.locators import LocatorsRegistration
from ui.pages.authorization import PageAuthorization
from ui.pages.home import PageHome
import allure


class PageRegistration(PageAuthorization):

    url = f'http://myapp:{MYAPP_PORT}/reg'
    locators = LocatorsRegistration()

    @allure.step('register a new user with name {username}, email {email} and password {password}')
    def register(self, username, email, password, is_password_confirmed):
        self.input(self.locators.INPUT_USERNAME, username)
        self.input(self.locators.INPUT_EMAIL, email)
        self.input(self.locators.INPUT_PASSWORD, password)
        if is_password_confirmed:
            self.input(self.locators.INPUT_PASSWORD_CONFIRM, password)
        self.click(self.locators.CHECKBOX_TERM)

        self.click(self.locators.BUTTON_SUBMIT)

        try:
            self.find(self.locators.INPUT_USERNAME, timeout=2)
        except TimeoutException:
            self.logger.info(f'registered as "{username}" with email "{email}" and password "{password}"')
            return PageHome(self.driver, self.logger)
