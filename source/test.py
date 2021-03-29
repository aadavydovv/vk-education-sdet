from base import Base
import locators
import pytest


class Tests(Base):
    @pytest.mark.UI
    def test_login(self):
        self.check_page('Войти')
        self.login()

        self.check_page('Выйти', 'Login failed')

    @pytest.mark.UI
    def test_logout(self):
        self.test_login()

        self.click(locators.LOCATOR_BUTTON_LOGOUT_MENU)
        self.click(locators.LOCATOR_BUTTON_LOGOUT)

        self.check_page('Войти', 'Logout failed')

    @pytest.mark.UI
    def test_edit_info(self):
        self.test_login()

        self.click(locators.LOCATOR_BUTTON_PROFILE)

        self.check_page('Контактная информация')
        self.edit_info()

    @pytest.mark.UI
    @pytest.mark.parametrize('section', ['segments', 'billing'])
    def test_visit_sections(self, section):
        self.test_login()

        if section == 'segments':
            self.click(locators.LOCATOR_BUTTON_SEGMENTS)
            self.check_page('Аудиторные сегменты')
        else:
            self.click(locators.LOCATOR_BUTTON_BILLING)
            self.check_page('Поступления и списания')
