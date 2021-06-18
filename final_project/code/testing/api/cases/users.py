from misc.constants import CONTROL_USER_USERNAME, CONTROL_USER_PASSWORD, VALID_PASSWORD
from cases.base import CaseAPIBase
from myapp_api.client import APIClient
import allure
from generators import make_email
import pytest


class CaseAPIUsers(CaseAPIBase):

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, logger):
        self.api_client = APIClient(logger)
        self.logger = logger

    # main methods

    @allure.step('add the user with username {username}')
    def add_user(self, username, password=None, email=None):
        if username or password or email:
            password = VALID_PASSWORD if (password is None) else password
            email = email if email else make_email(username)

        response = self.api_client.post_add_user(username, password, email)
        return response

    @allure.step('delete the user with username {username}')
    def delete_user(self, username):
        response = self.api_client.get_delete_user(username)
        return response

    @allure.step('block the user with username {username}')
    def block_user(self, username):
        response = self.api_client.get_block_user(username)
        return response

    @allure.step('accept the user with username {username}')
    def accept_user(self, username):
        response = self.api_client.get_accept_user(username)
        return response

    # auxiliary methods

    @allure.step('register the user with username {username}')
    def register_user(self, username):
        email = make_email(username)
        self.api_client.post_register_user(username, VALID_PASSWORD, email)

    @allure.step('authorize the control user')
    def authorize_control_user(self):
        self.api_client.post_authorize(CONTROL_USER_USERNAME, CONTROL_USER_PASSWORD)

    @allure.step('clear cookies')
    def clear_cookies(self):
        self.api_client.session.cookies.clear()
        self.logger.info(f'cleared cookies')
