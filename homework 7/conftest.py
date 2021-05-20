from mock import server
from mock.constants import *
from mock.logger import HTTPLogger
from pathlib import Path
from requests.exceptions import ConnectionError
import pytest
import requests
import time

homework_root = Path(__file__).parent


def mock_start():
    server.run()

    started = False
    start_time = time.time()

    while time.time() - start_time <= 5:
        try:
            requests.get(f'http://{MOCK_HOST}:{MOCK_PORT}')
            started = True
            break

        except ConnectionError:
            pass

    if not started:
        raise RuntimeError('mock failed to start in 5s')


def mock_stop():
    requests.get(f'http://{MOCK_HOST}:{MOCK_PORT}/shutdown')


@pytest.fixture(scope='session')
def logger():
    return HTTPLogger()


def pytest_configure(config):
    config.addinivalue_line('markers', 'Mock: mark test as mock test')

    if not hasattr(config, 'workerinput'):
        mock_start()


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        mock_stop()
