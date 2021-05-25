from mysql.models import Base
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
import sqlalchemy


class MySQLClient:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = '127.0.0.1'
        self.port = 3306

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_exists=True):
        db = self.db_name if db_exists else ''

        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}',
            encoding='utf8'
        )
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine, expire_on_commit=False)()

    def execute_query(self, query, fetch=True):
        result = self.connection.execute(query)

        if fetch:
            return result.fetchall()

    def recreate_db(self):
        self.connect(db_exists=False)

        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)

        self.connection.close()

    def create_table(self, name):
        if not inspect(self.engine).has_table(name):
            Base.metadata.tables[name].create(self.engine)
