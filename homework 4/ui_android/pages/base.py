from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from ui_android.locators import LocatorsBase

DEFAULT_AMOUNT_CLICK_RETRIES = 3
DEFAULT_AMOUNT_SWIPES = 10
DEFAULT_TIMEOUT = 5
DEFAULT_MESSAGE = 'unable to find "{}" by {}'
DEFAULT_SWIPE_DELAY = 2000


class PageBase(object):
    locators = LocatorsBase()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, message=DEFAULT_MESSAGE, timeout=DEFAULT_TIMEOUT):
        if message == DEFAULT_MESSAGE:
            message = message.format(locator[1], locator[0])

        return self.wait(timeout).until(ec.presence_of_element_located(locator), message=message)

    def wait(self, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def click(self, locator_element, swipe=False,
              locator_scroll=None, amount_swipes=DEFAULT_AMOUNT_SWIPES,
              amount_retries=DEFAULT_AMOUNT_CLICK_RETRIES, timeout=DEFAULT_TIMEOUT):
        if swipe:
            self.swipe_to_element(locator_element, locator_scroll, amount_swipes)

        for number_retry in range(1, amount_retries + 1):
            try:
                element = self.wait(timeout).until(ec.element_to_be_clickable(locator_element))
                element.click()
                return

            except StaleElementReferenceException:
                if number_retry == amount_retries - 1:
                    raise

    def swipe_to_element(self, locator_element, locator_scroll=None, amount_swipes=DEFAULT_AMOUNT_SWIPES):
        amount_swipes_done = 0

        while len(self.driver.find_elements(*locator_element)) == 0:
            if amount_swipes_done > amount_swipes:
                raise TimeoutException(f'swiped {amount_swipes} times'
                                       f' but did not find "{locator_element[1]}" by {locator_element[0]}')

            if locator_scroll:
                self.swipe_left(locator_scroll)
            else:
                self.swipe_up()

            amount_swipes_done += 1

    def swipe_left(self, locator_scroll, delay=DEFAULT_SWIPE_DELAY):
        element_scroll = self.find(locator_scroll)

        y_top = element_scroll.location['y']
        y_bottom = y_top + element_scroll.rect['height']
        y_middle = (y_top + y_bottom) / 2

        x_to = element_scroll.location['x']
        x_from = x_to + element_scroll.rect['width'] - 1

        self.swipe(x_from, x_to, y_middle, y_middle, delay)

    def swipe_up(self, delay=DEFAULT_SWIPE_DELAY):
        dimensions = self.driver.get_window_size()

        x = int(dimensions['width'] / 2)
        y_from = int(dimensions['height'] * 0.8)
        y_to = int(dimensions['height'] * 0.2)

        self.swipe(x, x, y_from, y_to, delay)

    def swipe(self, x_from, x_to, y_from, y_to, delay=DEFAULT_SWIPE_DELAY):
        action = TouchAction(self.driver)
        action. \
            press(x=x_from, y=y_from). \
            wait(ms=delay). \
            move_to(x=x_to, y=y_to). \
            release(). \
            perform()
