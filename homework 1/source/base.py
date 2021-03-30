from random_credentials import get_random_email
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
import locators
import pytest

AMOUNT_OF_RELOADS = 3
PAGE_CHECK_ERROR = 'Page failed to load properly'

# насчет ElementNotInteractableException:
# порой страницы загружались так, что определенный интерактивный элемент оказывался НЕинтерактивным
# так и не понял почему, однако рефреш всегда это фиксил
CLICK_EXCEPTIONS = (ElementNotInteractableException, StaleElementReferenceException)

# без некоторого ожидания после загрузки страницы порой недогружались(?)
# 3 секунды - минимальное значение, при котором тесты стабильно проходили
WAIT_TIME = 3


class Base:
    __driver = None
    credentials = {
        'login': None,
        'password': None,
        'fio': None,
        'phone': None
    }

    @pytest.fixture(scope='function', autouse=True)
    def __setup(self, driver, config):
        self.__driver = driver
        self.credentials['login'] = config['login']
        self.credentials['password'] = config['password']
        self.credentials['fio'] = config['fio']
        self.credentials['phone'] = config['phone']

    def __input(self, locator, data):
        form = self.__find(locator)
        form.clear()
        form.send_keys(data)

    def __input_random_emails(self):
        forms = self.__driver.find_elements(*locators.LOCATOR_INPUT_ADDITIONAL_EMAILS)
        email = get_random_email()

        for form in forms:
            form.clear()
            email[1] += 1
            form.send_keys(''.join(str(e) for e in email))

    def __reload(self, wait_time=WAIT_TIME):
        self.__driver.refresh()
        sleep(wait_time)

    def __find(self, locator):
        return self.__driver.find_element(*locator)

    def edit_info(self, amount_of_reloads=AMOUNT_OF_RELOADS, wait_time=WAIT_TIME):
        for n in range(amount_of_reloads + 1):
            try:
                self.__input(locators.LOCATOR_INPUT_FIO, self.credentials['fio'])
                self.__input(locators.LOCATOR_INPUT_PHONE, self.credentials['phone'])
                self.__input_random_emails()

                self.click(locators.LOCATOR_BUTTON_SAVE, 0)

            except CLICK_EXCEPTIONS:
                if n == amount_of_reloads:
                    raise

                self.__reload(wait_time)
                continue

            break

    def check_page(self, keyword, message=PAGE_CHECK_ERROR, amount_of_reloads=AMOUNT_OF_RELOADS,
                   wait_time=WAIT_TIME):
        for n in range(amount_of_reloads + 1):
            try:
                assert keyword in self.__driver.page_source, message

            except AssertionError:
                if n == amount_of_reloads:
                    raise

                self.__reload(wait_time)
                continue

            break

    def click(self, locator, amount_of_reloads=AMOUNT_OF_RELOADS, wait_time=WAIT_TIME):
        # пробовал вынести алгоритм ниже, также встречающийся в edit_info и check_page, в отдельный метод,
        # однако нехватило скилла, чтобы заставить селениум сотрудничать :(
        for n in range(amount_of_reloads + 1):
            try:
                self.__find(locator).click()

            except CLICK_EXCEPTIONS:
                if n == amount_of_reloads:
                    raise

                self.__reload(wait_time)
                continue

            break

        sleep(wait_time)

    def login(self):
        self.click(locators.LOCATOR_BUTTON_LOGIN_MENU)

        self.__input(locators.LOCATOR_INPUT_EMAIL, self.credentials['login'])
        self.__input(locators.LOCATOR_INPUT_PASSWORD, self.credentials['password'])

        self.click(locators.LOCATOR_BUTTON_LOGIN)
