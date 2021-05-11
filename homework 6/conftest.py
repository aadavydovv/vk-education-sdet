from mysql.client import MySQLClient
import pytest

# хардкод - исключительно следуя тз; в фикстуру выносить - нет смысла..?
SQL_USER = 'root'
SQL_PASSWORD = 'pass'
SQL_DB_NAME = 'TEST_SQL'


def pytest_addoption(parser):
    parser.addoption('--log_path', default='../misc/access.log')  # путь к логу от корня репы


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MySQLClient(user=SQL_USER, password=SQL_PASSWORD, db_name=SQL_DB_NAME)
        mysql_client.recreate_db()
        mysql_client.connect()

        mysql_client.create_table('amount_of_requests_overall')
        mysql_client.create_table('amount_of_requests_by_type')
        mysql_client.create_table('top_requests_by_url')
        mysql_client.create_table('top_requests_with_client_error_by_size')
        mysql_client.create_table('top_requests_with_server_error_by_ip')

        mysql_client.connection.close()


@pytest.fixture(scope='session')
def config(request):
    return {'log_path': request.config.getoption('--log_path')}


@pytest.fixture(scope='session')
def mysql_client():
    client = MySQLClient(user=SQL_USER, password=SQL_PASSWORD, db_name=SQL_DB_NAME)
    client.connect()
    yield client
    client.connection.close()
