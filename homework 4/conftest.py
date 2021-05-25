from ui_android.fixtures import *


def pytest_configure(config):
    config.addinivalue_line('markers', 'AndroidUI: mark test as Android UI test')


def pytest_addoption(parser):
    parser.addoption('--appium_server', default='http://localhost:4723/wd/hub')
    parser.addoption('--apk_path', default='misc/Marussia_v1.39.1.apk')  # относительно корня репозитория


@pytest.fixture(scope='session')
def config(request):
    return {
        'appium_server': request.config.getoption('--appium_server'),
        'apk_path': request.config.getoption('--apk_path')
    }
