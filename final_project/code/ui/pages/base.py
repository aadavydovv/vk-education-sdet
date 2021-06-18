from misc.constants import MYAPP_PORT
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators import LocatorsBase
import allure
import time

DEFAULT_AMOUNT_CLICK_RETRIES = 3
DEFAULT_TIMEOUT = 5
DEFAULT_MESSAGE = 'unable to find "{}" by {} at "{}"'


class PageOpenFailException(Exception):
    pass


class PageBase(object):

    url = f'http://myapp:{MYAPP_PORT}/'
    locators = LocatorsBase()

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

        self.logger.info(f'opening the page "{self.__class__.__name__}"')
        self._check_if_opened()

    def _check_if_opened(self):
        time_start = time.time()
        while time.time() - time_start < DEFAULT_TIMEOUT:
            if self.driver.current_url == self.url:
                self.logger.info(f'successfully checked that the page "{self.__class__.__name__}" has opened')
                return

            time.sleep(0.1)

        raise PageOpenFailException(
            f'"{self.url}" did not open in {DEFAULT_TIMEOUT} seconds for "{self.__class__.__name__}"\n'
            f'the current url is "{self.driver.current_url}"'
        )

    def _wait(self, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def _scroll_to(self, target):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', target)

    @allure.step('search for the element by the locator "{locator}"')
    def find(self, locator, message=DEFAULT_MESSAGE, timeout=DEFAULT_TIMEOUT, wait_until_visible=False):
        if message == DEFAULT_MESSAGE:
            message = message.format(locator[1], locator[0], self.driver.current_url)

        if wait_until_visible:
            condition = ec.visibility_of_element_located(locator)
        else:
            condition = ec.presence_of_element_located(locator)

        self.logger.info(f'searching for the element "{locator[1]}" (by {locator[0]}) with the timeout of {timeout}s')
        return self._wait(timeout).until(condition, message=message)

    @allure.step('click the element by the locator "{locator}"')
    def click(self, locator, timeout=DEFAULT_TIMEOUT, amount_retries=DEFAULT_AMOUNT_CLICK_RETRIES):
        for number_retry in range(1, amount_retries + 1):
            try:
                element = self.find(locator, timeout=timeout)
                self._scroll_to(element)

                element = self._wait(timeout).until(ec.element_to_be_clickable(locator))
                element.click()

                self.logger.info(f'clicked the element "{locator[1]}" (by {locator[0]})')

                return

            except StaleElementReferenceException:
                if number_retry == amount_retries - 1:
                    raise

    @allure.step('input {data} into the element by the locator "{locator}"')
    def input(self, locator, data, clear=True):
        form = self.find(locator)

        if clear:
            form.clear()

        form.send_keys(data)
        self.logger.info(f'inputted "{data}" into the element "{locator[1]}" (by {locator[0]})')
