from misc.constants import MYAPP_PORT, SELENOID_PORT
from selenium import webdriver
from ui.pages.login import PageLogin
import allure
import os
import pytest


@pytest.fixture
def page_login(driver, logger):
    return PageLogin(driver, logger)


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()

    capabilities = {
        'browserName': 'chrome',
        'version': '90.0',
        'sessionTimeout': '1m',
        'screenResolution': '1280x720x24'  # 720p/hd
    }

    browser = webdriver.Remote(f'http://selenoid:{SELENOID_PORT}/wd/hub', options=options,
                               desired_capabilities=capabilities)

    browser.maximize_window()
    browser.get(f'http://myapp:{MYAPP_PORT}/login')

    yield browser

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def browser_reporter(driver, request, path_directory_output):
    amount_tests_failed_pre_yield = request.session.testsfailed

    yield

    screenshot_name = 'failure.png'
    log_name = 'browser.log'

    if request.session.testsfailed > amount_tests_failed_pre_yield:
        path_screenshot = os.path.join(path_directory_output, screenshot_name)
        driver.get_screenshot_as_file(path_screenshot)
        allure.attach.file(path_screenshot, screenshot_name, attachment_type=allure.attachment_type.PNG)

        path_log_browser = os.path.join(path_directory_output, log_name)
        with open(path_log_browser, 'w') as file_log_browser:
            for i in driver.get_log('browser'):
                file_log_browser.write(f'{i["level"]} - {i["source"]}\n{i["message"]}\n\n')

        with open(path_log_browser, 'r') as file_log_browser:
            allure.attach(file_log_browser.read(), log_name, attachment_type=allure.attachment_type.TEXT)
