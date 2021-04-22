from selenium import webdriver
from ui.pages.auth import PageAuth
from ui.pages.base import PageBase
from ui.pages.post_auth import PagePostAuth
from webdriver_manager.chrome import ChromeDriverManager
import allure
import os
import pytest


@pytest.fixture(scope='function')
def page_base(driver):
    return PageBase(driver=driver)


@pytest.fixture(scope='function')
def page_auth(driver):
    return PageAuth(driver=driver)


# 2-ой пункт из UI части ТЗ
@pytest.fixture(scope='function')
def page_post_auth(page_auth, config):
    page_auth.log_in(config)
    return PagePostAuth(driver=page_auth.driver)


@pytest.fixture(scope='function')
def page_segments(page_post_auth):
    return page_post_auth.visit_segments()


@pytest.fixture(scope='function')
def page_campaign_creation(page_post_auth):
    return page_post_auth.start_campaign_creation()


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.headless = True

    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install(), options=options)

    browser.set_window_size(1280, 720)
    browser.get('https://target.my.com')

    yield browser

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def reporter(driver, request, path_directory_output):
    amount_tests_failed_pre_yield = request.session.testsfailed

    yield

    if request.session.testsfailed > amount_tests_failed_pre_yield:
        path_screenshot = os.path.join(path_directory_output, 'fail.png')
        driver.get_screenshot_as_file(path_screenshot)
        allure.attach.file(path_screenshot, 'fail.png', attachment_type=allure.attachment_type.PNG)

        path_log_browser = os.path.join(path_directory_output, 'browser.log')
        with open(path_log_browser, 'w') as file_log_browser:
            for i in driver.get_log('browser'):
                file_log_browser.write(f'{i["level"]} - {i["source"]}\n{i["message"]}\n\n')

        with open(path_log_browser, 'r') as file_log_browser:
            allure.attach(file_log_browser.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)


@pytest.fixture(scope='session')
def path_picture(path_directory_project):
    return os.path.join(path_directory_project, 'ui', 'picture.png')
