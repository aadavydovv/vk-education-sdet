from sqlalchemy import INTEGER, VARCHAR, SMALLINT, DATETIME, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'test_users'

    id = Column(INTEGER, nullable=False, autoincrement=True, primary_key=True)
    username = Column(VARCHAR(16), default=None, unique=True)
    password = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(64), nullable=False, unique=True)
    access = Column(SMALLINT, default=None)
    active = Column(SMALLINT, default=None)
    start_active_time = Column(DATETIME, default=None)
