from cases.login import CaseUILogin
import allure
import pytest

from misc.constants import (VALID_USERNAME, VALID_PASSWORD, CONTROL_USER_USERNAME, CONTROL_USER_PASSWORD,
                            INVALID_USERNAME_NONEXISTENT, ERROR_INVALID_USERNAME_OR_PASSWORD,
                            INVALID_USERNAME_TOO_SHORT, ERROR_USERNAME_LENGTH, INVALID_USERNAME_TOO_LONG,
                            ERROR_EMPTY_USERNAME, INVALID_PASSWORD_TOO_LONG, ERROR_PASSWORD_LENGTH,
                            ERROR_EMPTY_PASSWORD)


@allure.epic('myapp ui')
@allure.feature('login page')
class TestUILogin(CaseUILogin):

    @allure.title('valid credentials login test')
    def test_valid_credentials(self):
        """
        протестировать логин при валидных реквизитах

        шаги:
            1) ввести имя и пароль контрольного пользователя в соответствующие поля страницы логина
            2) кликнуть ссылку "login"
            3) осуществить поиск ссылки "logout"

        элемент со ссылкой должен быть обнаружен
        """
        page_home = self.page_login.log_in(CONTROL_USER_USERNAME, CONTROL_USER_PASSWORD)
        self.page_login.check_authorization(page_home=page_home)

    @allure.title('invalid credentials (nonexistent user) login test')
    def test_invalid_credentials_nonexistent_user(self):
        """
        протестировать логин при реквизитах несуществующего пользователя

        шаги:
            1) ввести имя и пароль несуществующего пользователя в соответствующие поля страницы логина
            2) кликнуть ссылку "login"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Invalid username or password"
        """
        self.page_login.log_in(username=INVALID_USERNAME_NONEXISTENT, password=VALID_PASSWORD)
        self.page_login.check_authorization(error_message=ERROR_INVALID_USERNAME_OR_PASSWORD)

    @allure.title('invalid credentials (username is too short) login test')
    def test_invalid_credentials_username_too_short(self):
        """
        протестировать логин при слишком коротком имени пользователя

        шаги:
            1) ввести слишком короткое имя пользователя и допустимый пароль в соответствующие поля страницы логина
            2) кликнуть ссылку "login"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Incorrect username length"
        """
        self.page_login.log_in(username=INVALID_USERNAME_TOO_SHORT, password=VALID_PASSWORD)
        self.page_login.check_authorization(error_message=ERROR_USERNAME_LENGTH)

    @allure.title('invalid credentials (username is too long) login test')
    def test_invalid_credentials_username_too_long(self):
        """
        протестировать логин при слишком длинном имени пользователя

        шаги:
            1) ввести слишком длинное имя пользователя и допустимый пароль в соответствующие поля страницы логина
            2) кликнуть ссылку "login"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно было бы содержать следующее: "Incorrect username length"
        """
        self.page_login.log_in(username=INVALID_USERNAME_TOO_LONG, password=VALID_PASSWORD)
        self.page_login.check_authorization(error_message=ERROR_USERNAME_LENGTH)

    @allure.title('invalid credentials (username is empty) login test')
    def test_invalid_credentials_username_empty(self):
        """
        протестировать логин при пустом имени пользователя

        шаги:
            1) ввести пустое имя пользователя и допустимый пароль в соответствующие поля страницы логина
            2) кликнуть ссылку "login"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Необходимо указать логин для авторизации"
        """
        self.page_login.log_in(username=' ', password=VALID_PASSWORD)
        self.page_login.check_authorization(error_message=ERROR_EMPTY_USERNAME)

    @allure.title('invalid credentials (password is too long) login test')
    def test_invalid_credentials_password_too_long(self):
        """
        протестировать логин при слишком длинном пароле

        шаги:
            1) ввести допустимое имя пользователя и слишком длинный пароль в соответствующие поля страницы логина
            2) кликнуть ссылку "login"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Incorrect password length"
        """
        self.page_login.log_in(username=VALID_USERNAME, password=INVALID_PASSWORD_TOO_LONG)
        self.page_login.check_authorization(error_message=ERROR_PASSWORD_LENGTH)

    @allure.title('invalid credentials (password is empty) login test')
    def test_invalid_credentials_password_empty(self):
        """
        протестировать логин при пустом пароле

        шаги:
            1) ввести допустимое имя пользователя и пустой пароль в соответствующие поля страницы логина
            2) кликнуть ссылку "login"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Необходимо указать пароль для авторизации"
        """
        self.page_login.log_in(username=VALID_USERNAME, password=' ')
        self.page_login.check_authorization(error_message=ERROR_EMPTY_PASSWORD)
