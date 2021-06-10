from misc.constants import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB_NAME, MYSQL_HOST, MYSQL_PORT
from sqlalchemy.orm import sessionmaker
import sqlalchemy


class MySQLClient:

    def __init__(self, user=MYSQL_USER, password=MYSQL_PASSWORD, db_name=MYSQL_DB_NAME,
                 host=MYSQL_HOST, port=MYSQL_PORT):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

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

    def disconnect(self):
        self.connection.close()
