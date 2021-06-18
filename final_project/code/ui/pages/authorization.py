from ui.pages.base import PageBase
from ui.pages.home import PageHome
import allure


class InvalidAuthorizationCheckUsage(Exception):
    pass


class PageAuthorization(PageBase):

    @allure.step('check if the authorization has succeeded or failed')
    def check_authorization(self, error_message=None, page_home: PageHome = None):
        if not (error_message or page_home):
            raise InvalidAuthorizationCheckUsage('neither error message nor home page instance was provided '
                                                 'for the authorization check')
        elif error_message and page_home:
            raise InvalidAuthorizationCheckUsage('both error message and home page instance were provided '
                                                 'for the authorization check')

        if error_message:
            assert error_message in self.find(
                self.locators.TEXT_ERROR, wait_until_visible=True).text, \
                'did not get the provided error message after the failed authorization'
        elif page_home:
            page_home.find(page_home.locators.BUTTON_LOGOUT)
