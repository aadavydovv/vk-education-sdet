from source.random_credentials import get_random_fio
from source.random_credentials import get_random_phone
from selenium import webdriver
import pytest


def pytest_configure(config):
    config.addinivalue_line('markers', 'UI: mark test as UI test')


def pytest_addoption(parser):
    parser.addoption('--login', default='x43872@gmail.com')
    parser.addoption('--password', default='GorhFabo6$Waso')
    parser.addoption('--fio', default=get_random_fio())
    parser.addoption('--phone', default=get_random_phone())


@pytest.fixture(scope='session')
def config(request):
    email = request.config.getoption('--login')
    password = request.config.getoption('--password')
    fio = request.config.getoption('--fio')
    phone = request.config.getoption('--phone')

    return {'login': email,
            'password': password,
            'fio': fio,
            'phone': phone}


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.headless = True

    browser = webdriver.Chrome(options=options, executable_path='/home/x/docs/education/mailru/misc/chromedriver')

    browser.set_window_size(1280, 720)  # для неизменности интерфейса
    browser.get('https://target.my.com/')

    yield browser

    browser.quit()
