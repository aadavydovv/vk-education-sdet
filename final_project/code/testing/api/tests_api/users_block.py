from cases.users import CaseAPIUsers
from generators import make_username
from misc.constants import STATUS_OK, STATUS_UNAUTHORIZED, STATUS_NOT_FOUND, STATUS_NOT_MODIFIED
import allure
import inspect
import pytest


@allure.epic('myapp api')
@allure.feature('user management - block')
class TestAPIUsersBlock(CaseAPIUsers):

    @allure.title('block accepted user test')
    def test_block_user_accepted(self):
        """
        протестировать блокировку незаблокированного пользователя

        шаги:
            1) зарегистрировать тестового пользователя
            2) заблокировать тестового пользователя
            3) проверить ответ на запрос

        ответ должен иметь статус 200 - действие выполнено
        """
        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        self.register_user(username)

        response = self.block_user(username)
        self.check_response_status(response, STATUS_OK)

    @allure.title('unauthorized block user test')
    def test_unauthorized_block_user(self):
        """
        протестировать блокировку пользователя без авторизации

        шаги:
            1) зарегистрировать тестового пользователя
            2) очистить куки
            3) заблокировать тестового пользователя
            4) проверить ответ на запрос

        ответ должен иметь статус 401 - пользователь не авторизован
        """
        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        self.register_user(username)

        self.clear_cookies()

        response = self.block_user(username)
        self.check_response_status(response, STATUS_UNAUTHORIZED)

    @allure.title('block nonexistent user test')
    def test_block_user_nonexistent(self):
        """
        протестировать блокировку несуществующего пользователя

        шаги:
            1) авторизовать контрольного пользователя
            2) заблокировать несуществующего пользователя
            3) проверить ответ на запрос

        ответ должен иметь статус 404 - сущности не существует
        """
        self.authorize_control_user()

        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        response = self.block_user(username)

        self.check_response_status(response, STATUS_NOT_FOUND)

    @allure.title('block blocked user test')
    def test_block_user_blocked(self):
        """
        протестировать блокировку заблокированного пользователя

        шаги:
            1) зарегистрировать тестового пользователя
            2) авторизовать контрольного пользователя
            3) заблокировать тестового пользователя
            4) ещё раз заблокировать тестового пользователя
            5) проверить ответ на запрос

        ответ должен иметь статус 304 - сущность существует или не изменилась
        """
        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        self.register_user(username)

        self.authorize_control_user()

        self.block_user(username)
        response = self.block_user(username)
        self.check_response_status(response, STATUS_NOT_MODIFIED)
