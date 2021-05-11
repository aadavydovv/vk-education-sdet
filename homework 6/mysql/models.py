from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AmountRequestsOverall(Base):
    __tablename__ = 'amount_of_requests_overall'

    amount = Column(Integer, primary_key=True)


class AmountRequestsByType(Base):
    __tablename__ = 'amount_of_requests_by_type'

    # не является обозначением порядка убывания, как в иных случаях
    number = Column('N', Integer, primary_key=True, autoincrement=True)

    type_request = Column('type', String(32), primary_key=False)
    amount = Column(Integer, primary_key=False)


class TopByUrl(Base):
    __tablename__ = 'top_requests_by_url'

    number = Column('N', Integer, primary_key=True, autoincrement=True)

    url = Column(String(512), primary_key=False)
    amount_requests = Column('amount_of_requests', Integer, primary_key=False)


class TopBySizeWithClientError(Base):
    __tablename__ = 'top_requests_with_client_error_by_size'

    number = Column('N', Integer, primary_key=True, autoincrement=True)

    url = Column(String(512), primary_key=False)
    status = Column(Integer, primary_key=False)
    size = Column(Integer, primary_key=False)
    ip = Column(String(16), primary_key=False)


class TopByIpWithServerError(Base):
    __tablename__ = 'top_requests_with_server_error_by_ip'

    number = Column('N', Integer, primary_key=True, autoincrement=True)

    ip = Column(String(16), primary_key=False)
    amount_requests = Column('amount_of_requests', Integer, primary_key=False)
