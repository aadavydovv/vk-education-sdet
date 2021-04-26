from appium import webdriver
from pathlib import Path
from ui_android.pages.assistant import PageAssistant
from ui_android.pages.settings import PageSettings
from ui_android.pages.settings_about import PageSettingsAbout
from ui_android.pages.settings_news import PageSettingsNews
import pytest


@pytest.fixture(scope='function')
def driver(config):
    appium_server = config['appium_server']

    path_repo = Path(__file__).parents[2]
    capabilities = {
        'platformName': 'Android',
        'platformVersion': '8.1',
        'automationName': 'Appium',
        'appPackage': 'ru.mail.search.electroscope',
        'appActivity': '.ui.activity.AssistantActivity',
        'app': f'{path_repo / config["apk_path"]}',
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
def page_settings_about(driver, config):
    return PageSettingsAbout(driver, config)
