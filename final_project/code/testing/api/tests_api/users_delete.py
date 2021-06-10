from cases.users import CaseAPIUsers
from generators import make_username
from misc.constants import STATUS_UNAUTHORIZED, STATUS_NOT_FOUND, STATUS_NO_CONTENT
import allure
import inspect
import pytest


@allure.epic('myapp api')
@allure.feature('user management - delete')
class TestAPIUsersDelete(CaseAPIUsers):

    @allure.title('delete existent user test')
    def test_delete_user_existent(self):
        """
        протестировать удаление существующего пользователя

        шаги:
            1) зарегистрировать тестового пользователя
            2) удалить тестового пользователя
            3) проверить ответ на запрос

        ответ должен иметь статус 204 - сущность удалена
        """
        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        self.register_user(username)

        response = self.delete_user(username)
        self.check_response_status(response, STATUS_NO_CONTENT)

    @allure.title('delete unauthorized user test')
    def test_unauthorized_delete_user(self):
        """
        протестировать удаление пользователя без авторизации

        шаги:
            1) зарегистрировать тестового пользователя
            2) очистить куки
            3) удалить тестового пользователя
            4) проверить ответ на запрос

        ответ должен иметь статус 401 - пользователь не авторизован
        """
        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        self.register_user(username)

        self.clear_cookies()

        response = self.delete_user(username)
        self.check_response_status(response, STATUS_UNAUTHORIZED)

    @allure.title('delete nonexistent user test')
    def test_delete_user_nonexistent(self):
        """
        протестировать удаление несуществующего пользователя

        шаги:
            1) авторизовать контрольного пользователя
            2) удалить несуществующего тестового пользователя
            3) проверить ответ на запрос

        ответ должен иметь статус 404 - сущности не существует
        """
        self.authorize_control_user()

        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        response = self.delete_user(username)

        self.check_response_status(response, STATUS_NOT_FOUND)
