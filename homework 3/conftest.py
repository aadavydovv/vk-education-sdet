import pytest


def pytest_configure(config):
    config.addinivalue_line('markers', 'API: mark test as API test')


def pytest_addoption(parser):
    parser.addoption('--login', default='x43872@gmail.com')
    parser.addoption('--password', default='GorhFabo6$Waso')


@pytest.fixture(scope='session')
def config(request):
    return {
        'login': request.config.getoption('--login'),
        'password': request.config.getoption('--password')
    }
