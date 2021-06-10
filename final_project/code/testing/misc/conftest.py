from fixtures import *
import allure
import logging
import os
import pytest
import shutil


def pytest_configure(config):
    config.addinivalue_line('python_files', '*.py')

    directory_output_base = '/tmp/testing_output'

    if not hasattr(config, 'workerinput'):
        if os.path.exists(directory_output_base):
            shutil.rmtree(directory_output_base)

        os.makedirs(directory_output_base)

    config.directory_output_base = directory_output_base


@pytest.fixture(scope='session')
def path_directory_project():
    return os.path.abspath(os.path.join(__file__, os.pardir))


@pytest.fixture(scope='function')
def path_directory_output(request):
    name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    path = os.path.join(request.config.directory_output_base, name)
    os.makedirs(path)
    return path


@pytest.fixture(scope='function', autouse=True)
def logger(path_directory_output):
    log_name = 'test.log'
    log_path = os.path.join(path_directory_output, log_name)

    formatter = logging.Formatter('%(asctime)s | %(filename)-16s | %(message)s')
    level = logging.INFO

    handler = logging.FileHandler(log_path, 'w')
    handler.setFormatter(formatter)
    handler.setLevel(level)

    logger = logging.getLogger('test')
    logger.propagate = False
    logger.setLevel(level)
    logger.handlers.clear()
    logger.addHandler(handler)

    yield logger

    for handler in logger.handlers:
        handler.close()

    with open(log_path, 'r') as log_file:
        allure.attach(log_file.read(), log_name, attachment_type=allure.attachment_type.TEXT)

