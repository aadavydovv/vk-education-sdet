from base import Base
import locators
import pytest


class Tests(Base):
    @pytest.mark.UI
    def test_login(self):
        self.login()
        self.find(locators.LOCATOR_BUTTON_LOGOUT_MENU, 'Login failed')

    @pytest.mark.UI
    def test_logout(self):
        self.test_login()

        self.click(locators.LOCATOR_BUTTON_LOGOUT_MENU)
        self.click(locators.LOCATOR_BUTTON_LOGOUT)

        self.find(locators.LOCATOR_BUTTON_LOGIN_MENU, 'Logout failed')

    @pytest.mark.UI
    def test_edit_info(self):
        self.test_login()

        self.click(locators.LOCATOR_BUTTON_PROFILE)

        new_fio = self.edit_info()
        self.check_edited_info(new_fio)

    @pytest.mark.UI
    @pytest.mark.parametrize(
        'locator_button, locator_control', [
            (locators.LOCATOR_BUTTON_SEGMENTS, locators.LOCATOR_TEXT_CONTROL_SEGMENTS),
            (locators.LOCATOR_BUTTON_BILLING, locators.LOCATOR_TEXT_CONTROL_BILLING)
        ]
    )
    def test_visit_section(self, locator_button, locator_control):
        self.test_login()
        self.click(locator_button)
        self.find(locator_control, 'Failed to visit section')
