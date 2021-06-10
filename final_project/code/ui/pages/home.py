from misc.constants import MYAPP_PORT
from selenium.webdriver import ActionChains
from ui.locators import LocatorsHome
from ui.pages.base import PageBase
import allure


class InvalidLoginInfoCheckUsage(Exception):
    pass


class PageHome(PageBase):

    url = f'http://myapp:{MYAPP_PORT}/welcome/'
    locators = LocatorsHome()

    @allure.step('log out')
    def log_out(self):
        self.click(self.locators.BUTTON_LOGOUT)
        self.logger.info('logged out')

    @allure.step('check the login info')
    def check_login_info(self, user_name=None, user_id=None):
        if not (user_name or user_id):
            raise InvalidLoginInfoCheckUsage('neither user name nor user id was provided for '
                                             'the login info check method')
        elif user_name and user_id:
            raise InvalidLoginInfoCheckUsage('both user name and user id were provided for '
                                             'the login info check method')

        login_info = self.find(self.locators.TEXT_LOGIN_NAME).text

        if user_name:
            assert f'Logged as {user_name}' in login_info
        elif user_id:
            assert f'VK ID: {user_id}' in login_info

    @property
    def action_chains(self):
        return ActionChains(self.driver)

    @allure.step('open the menu by the locator "{menu_locator}"')
    def open_menu(self, menu_locator):
        menu = self.find(menu_locator)
        self.action_chains.move_to_element(menu).perform()
