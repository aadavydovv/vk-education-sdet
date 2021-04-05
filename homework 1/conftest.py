from selenium import webdriver
import pytest


def pytest_configure(config):
    config.addinivalue_line('markers', 'UI: mark test as UI test')


def pytest_addoption(parser):
    parser.addoption('--login', default='x43872@gmail.com')
    parser.addoption('--password', default='GorhFabo6$Waso')


@pytest.fixture(scope='session')
def config(request):
    return {
        'login': request.config.getoption('--login'),
        'password': request.config.getoption('--password')
    }


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.headless = True

    browser = webdriver.Chrome(options=options, executable_path='/home/x/docs/education/mailru/misc/chromedriver')

    browser.set_window_size(1280, 720)  # для неизменности интерфейса
    browser.get('https://target.my.com/')

    yield browser

    browser.quit()
