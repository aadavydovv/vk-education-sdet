from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators import LocatorsBase
from utils.decorators import wait
import allure
import logging

DEFAULT_AMOUNT_CLICK_RETRIES = 3
DEFAULT_TIMEOUT = 5
DEFAULT_MESSAGE = 'unable to find "{}" by {} at "{}"'

LOGGER = logging.getLogger('test')


class PageOpenFailException(Exception):
    pass


class PageBase(object):
    url = 'https://target.my.com/'
    locators = LocatorsBase()

    def __init__(self, driver):
        self.driver = driver
        LOGGER.info(f'opening page "{self.__class__.__name__}"')
        assert self.is_opened()

    def is_opened(self):
        def _check_url():
            if self.driver.current_url != self.url:
                raise PageOpenFailException(
                    f'"{self.url}" did not open in {DEFAULT_TIMEOUT} seconds for "{self.__class__.__name__}" '
                    f'(current url: {self.driver.current_url})'
                )

            return True

        return wait(_check_url, exception=PageOpenFailException, check_result=True, timeout=DEFAULT_TIMEOUT,
                    delay_retry=0.1)

    def find(self, locator, message=DEFAULT_MESSAGE, timeout=DEFAULT_TIMEOUT):
        if message == DEFAULT_MESSAGE:
            message = message.format(locator[1], locator[0], self.driver.current_url)

        return self.wait(timeout).until(ec.presence_of_element_located(locator), message=message)

    def wait(self, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def scroll_to(self, target):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', target)

    @allure.step('clicking "{locator}"')
    def click(self, locator, timeout=DEFAULT_TIMEOUT, amount_retries=DEFAULT_AMOUNT_CLICK_RETRIES):
        for number_retry in range(1, amount_retries + 1):
            LOGGER.info(f'clicking "{locator[1]}" by {locator[0]}, retry {number_retry} of {amount_retries}')

            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)

                element = self.wait(timeout).until(ec.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if number_retry == amount_retries - 1:
                    raise

    @allure.step('inputting "{data}" into "{locator}"')
    def input(self, locator, data, clear=True):
        form = self.find(locator)

        if clear:
            form.clear()

        form.send_keys(data)
