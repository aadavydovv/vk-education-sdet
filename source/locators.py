from selenium.webdriver.common.by import By


LOCATOR_BUTTON_LOGIN = (By.XPATH, '//div[h3="Вход в рекламный кабинет"]//div[text()="Войти"]')

# "div" вместо "*" по непонятной мне причине рандомно фейлил
LOCATOR_BUTTON_LOGIN_MENU = (By.XPATH, '//*[text()="Войти"]')

LOCATOR_BUTTON_LOGOUT = (By.XPATH, '//a[text()="Выйти"]')
LOCATOR_BUTTON_LOGOUT_MENU = (By.XPATH, '//div[text()="Баланс: "]/../..')

LOCATOR_BUTTON_BILLING = (By.XPATH, '//a[text()="Баланс"]')
LOCATOR_BUTTON_PROFILE = (By.XPATH, '//a[text()="Профиль"]')
LOCATOR_BUTTON_SEGMENTS = (By.XPATH, '//a[text()="Аудитории"]')

LOCATOR_BUTTON_SAVE = (By.XPATH, '//button[div="Сохранить"]')

LOCATOR_INPUT_EMAIL = (By.XPATH, '//input[@name="email"]')
LOCATOR_INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')

LOCATOR_INPUT_ADDITIONAL_EMAILS = (By.XPATH, '//div[@data-class-name="AdditionalEmailRow"]//input')
LOCATOR_INPUT_FIO = (By.XPATH, '//div[@data-name="fio"]//input')
LOCATOR_INPUT_PHONE = (By.XPATH, '//div[@data-name="phone"]//input')
