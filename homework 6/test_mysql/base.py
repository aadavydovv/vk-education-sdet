from mysql.builder import MySQLBuilder
from test_mysql.script import Script
import pytest


class MySQLBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, mysql_client):
        self.mysql_client = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.script = Script(config['log_path'])
