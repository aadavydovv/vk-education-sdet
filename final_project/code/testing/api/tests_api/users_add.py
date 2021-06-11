from cases.base import UnexpectedResponseStatusException
from cases.users import CaseAPIUsers
from generators import make_username
import allure
import inspect
import pytest

from misc.constants import (STATUS_UNAUTHORIZED, STATUS_NOT_MODIFIED, STATUS_CREATED, STATUS_BAD_REQUEST,
                            INVALID_USERNAME_TOO_SHORT, INVALID_USERNAME_TOO_LONG, INVALID_EMAIL_TOO_SHORT, INVALID_EMAIL_TOO_LONG,
                            INVALID_EMAIL_FORMAT, INVALID_PASSWORD_TOO_LONG)


@allure.epic('myapp api')
@allure.feature('user management - add')
class TestAPIUsersAdd(CaseAPIUsers):

    @allure.title('add valid user test')
    def test_add_user_valid(self):
        """
        протестировать добавление пользователя с валидными данными

        шаги:
            1) авторизовать контрольного пользователя
            2) добавить пользователя с валидными данными
            3) проверить ответ на запрос

        ответ должен иметь статус 201 - сущность создана
        """
        self.authorize_control_user()

        username = make_username()
        response = self.add_user(username)

        self.check_response_status(response, STATUS_CREATED)

    @allure.title('unauthorized add user test')
    def test_unauthorized_add_user(self):
        """
        протестировать добавление пользователя без авторизации

        шаги:
            1) добавить пользователя с валидными данными
            2) проверить ответ на запрос

        ответ должен иметь статус 401 - пользователь не авторизован
        """
        username = make_username()
        response = self.add_user(username)

        self.check_response_status(response, STATUS_UNAUTHORIZED)

    @allure.title('add user with invalid name (too short) test')
    def test_add_user_invalid_name_too_short(self):
        """
        протестировать добавление пользователя при слишком коротком имени

        шаги:
            1) авторизовать контрольного пользователя
            2) добавить пользователя, указав слишком короткое имя
            3) проверить ответ на запрос

        ответ должен иметь статус 400 - плохой запрос
        """
        self.authorize_control_user()

        response = self.add_user(INVALID_USERNAME_TOO_SHORT)
        self.check_response_status(response, STATUS_BAD_REQUEST)

    @allure.title('add user with invalid name (too long) test')
    def test_add_user_invalid_name_too_long(self):
        """
        протестировать добавление пользователя при слишком длинном имени

        шаги:
            1) авторизовать контрольного пользователя
            2) добавить пользователя, указав слишком длинное имя
            3) проверить ответ на запрос

        ответ должен иметь статус 400 - плохой запрос
        """
        self.authorize_control_user()

        response = self.add_user(INVALID_USERNAME_TOO_LONG)
        #with pytest.raises(UnexpectedResponseStatusException):
        self.check_response_status(response, STATUS_BAD_REQUEST)

    @allure.title('add user with invalid email (too short) test')
    def test_add_user_invalid_email_too_short(self):
        """
        протестировать добавление пользователя при слишком коротком адресе эл. почты

        шаги:
            1) авторизовать контрольного пользователя
            2) добавить пользователя, указав слишком короткий адрес эл. почты
            3) проверить ответ на запрос

        ответ должен иметь статус 400 - плохой запрос
        """
        self.authorize_control_user()

        username = make_username()
        response = self.add_user(username, email=INVALID_EMAIL_TOO_SHORT)

        self.check_response_status(response, STATUS_BAD_REQUEST)

    @allure.title('add user with invalid email (too long) test')
    def test_add_user_invalid_email_too_long(self):
        """
        протестировать добавление пользователя при слишком длинном адресе эл. почты

        шаги:
            1) авторизовать контрольного пользователя
            2) добавить пользователя, указав слишком длинный адрес эл. почты
            3) проверить ответ на запрос

        ответ должен иметь статус 400 - плохой запрос
        """
        self.authorize_control_user()

        username = make_username()
        response = self.add_user(username, email=INVALID_EMAIL_TOO_LONG)

        #with pytest.raises(UnexpectedResponseStatusException):
        self.check_response_status(response, STATUS_BAD_REQUEST)

    @allure.title('add user with invalid email (bad format) test')
    def test_add_user_invalid_email_bad_format(self):
        """
        протестировать добавление пользователя при невалидном адресе эл. почты

        шаги:
            1) авторизовать контрольного пользователя
            2) добавить пользователя, указав невалидный адрес эл. почты
            3) проверить ответ на запрос

        ответ должен иметь статус 400 - плохой запрос
        """
        self.authorize_control_user()

        username = make_username()
        response = self.add_user(username, email=INVALID_EMAIL_FORMAT)

        self.check_response_status(response, STATUS_BAD_REQUEST)

    @allure.title('add user with invalid password (empty) test')
    def test_add_user_invalid_password_empty(self):
        """
        протестировать добавление пользователя при пустом пароле

        шаги:
            1) авторизовать контрольного пользователя
            2) добавить пользователя, указав пустой пароль
            3) проверить ответ на запрос

        ответ должен иметь статус 400 - плохой запрос
        """
        self.authorize_control_user()

        username = make_username()
        response = self.add_user(username, password='')

        self.check_response_status(response, STATUS_BAD_REQUEST)

    @allure.title('add user with invalid password (too long) test')
    def test_add_user_invalid_password_too_long(self):
        """
        протестировать добавление пользователя при слишком длинном пароле

        шаги:
            1) авторизовать контрольного пользователя
            2) добавить пользователя, указав слишком длинный пароль
            3) проверить ответ на запрос

        ответ должен иметь статус 400 - плохой запрос
        """
        self.authorize_control_user()

        username = make_username()
        response = self.add_user(username, password=INVALID_PASSWORD_TOO_LONG)

        self.check_response_status(response, STATUS_BAD_REQUEST)

    @allure.title('add existing user test')
    def test_add_existing_user(self):
        """
        протестировать добавление существующего пользователя

        шаги:
            1) зарегистрировать тестового пользователя
            2) добавить пользователя с аналогичными данными
            3) проверить ответ на запрос

        ответ должен иметь статус 304 - сущность существует или не изменилась
        """
        username = make_username()
        self.register_user(username)

        response = self.add_user(username)
        self.check_response_status(response, STATUS_NOT_MODIFIED)

    @allure.title('add user by bad request test')
    def test_add_user_bad_request(self):
        """
        протестировать добавление пользователя при невалидном запросе

        шаги:
            1) авторизовать контрольного пользователя
            2) добавить пользователя, указав пустое тело для запроса
            3) проверить ответ на запрос

        ответ должен иметь статус 400 - плохой запрос
        """
        self.authorize_control_user()
        response = self.add_user(None)
        self.check_response_status(response, STATUS_BAD_REQUEST)
