from appium import webdriver
from pathlib import Path
from ui_android.pages.assistant import PageAssistant
from ui_android.pages.settings import PageSettings
from ui_android.pages.settings_about import PageSettingsAbout
from ui_android.pages.settings_news import PageSettingsNews
import pytest


@pytest.fixture(scope='function')
def driver(config, apk_path):
    appium_server = config['appium_server']

    capabilities = {
        'platformName': 'Android',
        'platformVersion': '8.1',
        'automationName': 'Appium',
        'appPackage': 'ru.mail.search.electroscope',
        'appActivity': '.ui.activity.AssistantActivity',
        'app': str(apk_path),
        'orientation': 'PORTRAIT',
        'autoGrantPermissions': True
    }

    driver = webdriver.Remote(appium_server, desired_capabilities=capabilities)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def page_assistant(driver):
    return PageAssistant(driver)


@pytest.fixture(scope='function')
def page_settings(driver):
    return PageSettings(driver)


@pytest.fixture(scope='function')
def page_settings_news(driver):
    return PageSettingsNews(driver)


@pytest.fixture(scope='function')
def page_settings_about(driver, apk_path):
    return PageSettingsAbout(driver, apk_path)


@pytest.fixture(scope='session')
def apk_path(config):
    return Path.joinpath(Path(__file__).parents[2], config['apk_path'])
