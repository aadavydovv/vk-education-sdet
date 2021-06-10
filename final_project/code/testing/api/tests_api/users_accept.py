from cases.users import CaseAPIUsers
from generators import make_username
from misc.constants import STATUS_OK, STATUS_UNAUTHORIZED, STATUS_NOT_FOUND, STATUS_NOT_MODIFIED
import allure
import inspect
import pytest


@allure.epic('myapp api')
@allure.feature('user management - accept')
class TestAPIUsersAccept(CaseAPIUsers):

    @allure.title('accept blocked user test')
    def test_accept_user_blocked(self):
        """
        протестировать разблокировку заблокированного пользователя

        шаги:
            1) зарегистрировать тестового пользователя
            2) заблокировать тестового пользователя
            3) авторизовать контрольного пользователя
            4) разблокировать тестового пользователя
            5) проверить ответ на запрос

        ответ должен иметь статус 200 - действие выполнено
        """
        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        self.register_user(username)
        self.block_user(username)

        self.authorize_control_user()

        response = self.accept_user(username)
        self.check_response_status(response, STATUS_OK)

    @allure.title('unauthorized accept user test')
    def test_unauthorized_accept_user(self):
        """
        протестировать разблокировку пользователя без авторизации

        шаги:
            1) зарегистрировать тестового пользователя
            2) заблокировать тестового пользователя
            3) разблокировать тестового пользователя
            4) проверить ответ на запрос

        ответ должен иметь статус 401 - пользователь не авторизован
        """
        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        self.register_user(username)
        self.block_user(username)

        response = self.accept_user(username)
        self.check_response_status(response, STATUS_UNAUTHORIZED)

    @allure.title('accept nonexistent user test')
    def test_accept_user_nonexistent(self):
        """
        протестировать разблокировку несуществующего пользователя

        шаги:
            1) авторизовать контрольного пользователя
            2) разблокировать несуществующего пользователя
            3) проверить ответ на запрос

        ответ должен иметь статус 404 - сущности не существует
        """
        self.authorize_control_user()

        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        response = self.accept_user(username)

        self.check_response_status(response, STATUS_NOT_FOUND)

    @allure.title('accept accepted user test')
    def test_accept_user_accepted(self):
        """
        протестировать разблокировку незаблокированного пользователя

        шаги:
            1) зарегистрировать тестового пользователя
            2) разблокировать тестового пользователя
            3) проверить ответ на запрос

        ответ должен иметь статус 304 - сущность существует или не изменилась
        """
        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        self.register_user(username)

        response = self.accept_user(username)
        self.check_response_status(response, STATUS_NOT_MODIFIED)
