from cases.registration import CaseUIRegistration
from generators import make_username, make_email
from selenium.common.exceptions import TimeoutException
import allure
import inspect
import pytest

from misc.constants import (VALID_USERNAME, VALID_PASSWORD, VALID_EMAIL, CONTROL_USER_USERNAME, CONTROL_USER_EMAIL,
                            ERROR_USER_EXISTS, ERROR_USERNAME_LENGTH, ERROR_PASSWORD_LENGTH, ERROR_PASSWORD_MATCH,
                            ERROR_EMAIL_LENGTH, ERROR_EMAIL_INVALID, INVALID_USERNAME_TOO_SHORT,
                            INVALID_USERNAME_TOO_LONG, INVALID_PASSWORD_TOO_LONG, INVALID_EMAIL_TOO_SHORT,
                            INVALID_EMAIL_TOO_LONG, INVALID_EMAIL_FORMAT)


@allure.epic('myapp ui')
@allure.feature('registration page')
class TestUIRegistration(CaseUIRegistration):

    @allure.title('valid credentials registration test')
    def test_valid_credentials(self):
        """
        протестировать регистрацию при валидных реквизитах

        шаги:
            1) ввести валидные имя, адрес эл. почты и пароль в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск ссылки "logout"

        элемент со ссылкой должен быть обнаружен
        """
        test_name = inspect.currentframe().f_code.co_name
        username = make_username(test_name)
        email = make_email(username)
        page_home = self.page_registration.register(username=username, email=email,
                                                    password=VALID_PASSWORD, is_password_confirmed=True)
        self.page_registration.check_authorization(page_home=page_home)

    @allure.title('invalid credentials (existent user\'s username) registration test')
    def test_invalid_credentials_existent_user_username(self):
        """
        протестировать регистрацию при имени существующего пользователя

        шаги:
            1) ввести имя существующего пользователя и валидные адрес эл. почты и пароль в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "User already exist"
        """
        self.page_registration.register(username=CONTROL_USER_USERNAME, email=VALID_EMAIL,
                                        password=VALID_PASSWORD, is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_USER_EXISTS)

    @allure.title('invalid credentials (existent user\'s email) registration test')
    def test_invalid_credentials_existent_user_email(self):
        """
        протестировать регистрацию при адресе эл. почты существующего пользователя

        шаги:
            1) ввести адрес эл. почты существующего пользователя и валидные имя и пароль в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "User already exist"
        """
        self.page_registration.register(username=VALID_USERNAME, email=CONTROL_USER_EMAIL,
                                        password=VALID_PASSWORD, is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_USER_EXISTS)

    @allure.title('invalid credentials (username is too short) registration test')
    def test_invalid_credentials_username_too_short(self):
        """
        протестировать регистрацию при слишком коротком имени пользователя

        шаги:
            1) ввести слишком короткое имя пользователя и валидные адрес эл. почты и пароль в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Incorrect username length"
        """
        self.page_registration.register(username=INVALID_USERNAME_TOO_SHORT, email=VALID_EMAIL,
                                        password=VALID_PASSWORD, is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_USERNAME_LENGTH)

    @allure.title('invalid credentials (username is too long) registration test')
    def test_invalid_credentials_username_too_long(self):
        """
        протестировать регистрацию при слишком длинном имени пользователя

        шаги:
            1) ввести слишком длинное имя пользователя и валидные адрес эл. почты и пароль в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Incorrect username length"
        """
        self.page_registration.register(username=INVALID_USERNAME_TOO_LONG, email=VALID_EMAIL,
                                        password=VALID_PASSWORD, is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_USERNAME_LENGTH)

    @allure.title('invalid credentials (username is empty) registration test')
    def test_invalid_credentials_username_empty(self):
        """
        протестировать регистрацию при пустом имени пользователя

        шаги:
            1) ввести пустое имя пользователя и валидные адрес эл. почты и пароль в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Incorrect username length"
        """
        self.page_registration.register(username=' ', email=VALID_EMAIL,
                                        password=VALID_PASSWORD, is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_USERNAME_LENGTH)

    @allure.title('invalid credentials (password is too long) registration test')
    def test_invalid_credentials_password_too_long(self):
        """
        протестировать регистрацию при слишком длинном пароле

        шаги:
            1) ввести слишком длинный пароль и валидные имя пользователя и адрес эл. почты в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Incorrect password length"
        """
        self.page_registration.register(username=VALID_USERNAME, email=VALID_EMAIL,
                                        password=INVALID_PASSWORD_TOO_LONG, is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_PASSWORD_LENGTH)

    @allure.title('invalid credentials (password is empty) registration test')
    def test_invalid_credentials_password_empty(self):
        """
        протестировать регистрацию при пустом пароле

        шаги:
            1) ввести пустой пароль и валидные имя пользователя и адрес эл. почты в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Incorrect password length"
        """
        self.page_registration.register(username=VALID_USERNAME, email=VALID_EMAIL,
                                        password=' ', is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_PASSWORD_LENGTH)

    @allure.title('invalid credentials (no password confirmation) registration test')
    def test_invalid_credentials_password_no_confirmation(self):
        """
        протестировать регистрацию без подтверждения пароля

        шаги:
            1) заполнить все поля страницы регистрации валидными данными, не заполняя при этом подтверждение пароля
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Passwords must match"
        """
        self.page_registration.register(username=VALID_USERNAME, email=VALID_EMAIL,
                                        password=VALID_PASSWORD, is_password_confirmed=False)
        self.page_registration.check_authorization(error_message=ERROR_PASSWORD_MATCH)

    @allure.title('invalid credentials (email is too short) registration test')
    def test_invalid_credentials_email_too_short(self):
        """
        протестировать регистрацию при слишком коротком адресе эл. почты

        шаги:
            1) ввести слишком короткий адрес эл. почты и валидные имя пользователя и пароль в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Incorrect email length"
        """
        self.page_registration.register(username=VALID_USERNAME, email=INVALID_EMAIL_TOO_SHORT,
                                        password=VALID_PASSWORD, is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_EMAIL_LENGTH)

    @allure.title('invalid credentials (email is too long) registration test')
    def test_invalid_credentials_email_too_long(self):
        """
        протестировать регистрацию при слишком длинном адресе эл. почты

        шаги:
            1) ввести слишком длинный адрес эл. почты и валидные имя пользователя и пароль в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Incorrect email length"
        """
        self.page_registration.register(username=VALID_USERNAME, email=INVALID_EMAIL_TOO_LONG,
                                        password=VALID_PASSWORD, is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_EMAIL_LENGTH)

    @allure.title('invalid credentials (email is empty) registration test')
    def test_invalid_credentials_email_empty(self):
        """
        протестировать регистрацию при пустом адресе эл. почты

        шаги:
            1) ввести пустой адрес эл. почты и валидные имя пользователя и пароль в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Incorrect email length"
        """
        self.page_registration.register(username=VALID_USERNAME, email=' ',
                                        password=VALID_PASSWORD, is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_EMAIL_LENGTH)

    @allure.title('invalid credentials (email format is bad) registration test')
    def test_invalid_credentials_email_bad_format(self):
        """
        протестировать регистрацию при невалидном адресе эл. почты

        шаги:
            1) ввести невалидный адрес эл. почты и валидные имя пользователя и пароль в соответствующие поля страницы регистрации
            2) кликнуть ссылку "register"
            3) осуществить поиск сообщения об ошибке

        сообщение об ошибке должно содержать следующее: "Invalid email address"
        """
        self.page_registration.register(username=VALID_USERNAME, email=INVALID_EMAIL_FORMAT,
                                        password=VALID_PASSWORD, is_password_confirmed=True)
        self.page_registration.check_authorization(error_message=ERROR_EMAIL_INVALID)
