from selenium.webdriver.common.by import By


class LocatorsBase:
    TEXT_SUCCESS = (By.XPATH, '//*[contains(@class, "notify-module-success")]')

    @staticmethod
    def entry_by_title(title):
        return By.XPATH, f'//div[a="{title}"]'


class LocatorsAuth(LocatorsBase):
    BUTTON_LOG_IN = (By.XPATH, '//div[h3="Вход в рекламный кабинет"]//div[text()="Войти"]')
    BUTTON_LOG_IN_MENU = (By.XPATH, '//*[text()="Войти"]')

    INPUT_LOGIN = (By.XPATH, '//input[@name="email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')


class LocatorsPostAuth(LocatorsBase):
    BUTTON_CREATE_CAMPAIGN_FIRST = (By.XPATH, '//a[contains(@href, "/campaign/new")]')
    BUTTON_CREATE_CAMPAIGN_SUBSEQUENT = (By.XPATH, '//div[text()="Создать кампанию"]')

    BUTTON_SEGMENTS = (By.XPATH, '//a[contains(@href, "/segments")]')


class LocatorsSegments(LocatorsBase):
    BUTTON_CREATE_FIRST_SEGMENT = (By.XPATH, '//a[text()="Создайте"]')
    BUTTON_CREATE_SUBSEQUENT_SEGMENT = (By.XPATH, '//button[div="Создать сегмент"]')

    BUTTON_ADD_SEGMENT = (By.XPATH, '//button[div="Добавить сегмент"]')
    BUTTON_CHOOSE_SEGMENT = (By.XPATH, '//input[@type="checkbox"]')
    BUTTON_CHOOSE_SEGMENT_GROUP = (By.XPATH, '//div[text()="Приложения и игры в соцсетях"]')
    BUTTON_FINISH_CREATION = (By.XPATH, '//button[div="Создать сегмент"]')
    INPUT_SEGMENT_NAME = (By.XPATH, '//div[@class="js-segment-name"]//input')

    BUTTON_ACTIONS = (By.XPATH, '//div[span="Действия"]')
    BUTTON_DELETE_SEGMENT = (By.XPATH, '//li[@title="Удалить"]')

    BUTTON_FIRST_SEGMENT = (By.XPATH, '//div[@data-row-id="central-0"]//input')
    TEXT_FIRST_SEGMENT = (By.XPATH, '//a[contains(@href, "segments_list") and @title]')


class LocatorsCampaignCreation(LocatorsBase):
    BUTTON_FINISH_CREATION = (By.XPATH, '//button[div="Создать кампанию"]')
    BUTTON_FORMAT_BANNER = (By.ID, 'patterns_4')
    BUTTON_GOAL_TRAFFIC = (By.XPATH, '//div[contains(@class, "_traffic")]')

    INPUT_AD_URL = (By.XPATH, '//input[@data-gtm-id="ad_url_text"]')
    INPUT_NAME = (By.XPATH, '//div[contains(@class, "input_campaign-name")]//input')
    INPUT_PICTURE = (By.XPATH, '//input[@data-test="image_240x400"]')
