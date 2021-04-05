from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import locators
import pytest
import random_credentials as rc

AMOUNT_OF_RELOADS = 3
CLICK_EXCEPTIONS = (ElementNotInteractableException, StaleElementReferenceException)
DEFAULT_MESSAGE = 'Page failed to load properly'
TIME_WAIT = 5
TIME_SLEEP = 3


class Base:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

    def input(self, locator, data):
        form = self.find(locator)
        form.clear()
        form.send_keys(data)

    def input_random_emails(self):
        forms = self.driver.find_elements(*locators.LOCATOR_INPUT_ADDITIONAL_EMAILS)
        email = rc.get_random_email()

        for form in forms:
            form.clear()
            email[1] += 1
            form.send_keys(''.join(str(e) for e in email))

    def reload(self):
        self.driver.refresh()
        sleep(TIME_SLEEP)

    def find(self, locator, message=DEFAULT_MESSAGE):
        return self.wait().until(ec.presence_of_element_located(locator), message=message)

    def wait(self):
        return WebDriverWait(self.driver, timeout=TIME_WAIT)

    def edit_info(self):
        self.find(locators.LOCATOR_INPUT_FIO)

        new_fio = rc.get_random_fio()

        self.input(locators.LOCATOR_INPUT_FIO, new_fio)
        self.input(locators.LOCATOR_INPUT_PHONE, rc.get_random_phone())
        self.input_random_emails()

        self.click(locators.LOCATOR_BUTTON_SAVE)

        return new_fio

    def check_edited_info(self, fio_new):
        self.driver.refresh()
        fio_after_refresh = self.find(locators.LOCATOR_INPUT_FIO).get_attribute('value')
        assert fio_after_refresh == fio_new, 'Failed to edit info'

    def click(self, locator):
        for n in range(AMOUNT_OF_RELOADS + 1):
            try:
                self.find(locator).click()

            except CLICK_EXCEPTIONS:
                if n == AMOUNT_OF_RELOADS:
                    raise

                self.reload()
                continue

            break

        sleep(TIME_SLEEP)

    def login(self):
        self.click(locators.LOCATOR_BUTTON_LOGIN_MENU)

        self.input(locators.LOCATOR_INPUT_EMAIL, self.config['login'])
        self.input(locators.LOCATOR_INPUT_PASSWORD, self.config['password'])

        self.click(locators.LOCATOR_BUTTON_LOGIN)
