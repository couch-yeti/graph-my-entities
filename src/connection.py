import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from contextlib import contextmanager

load_dotenv()
connection_string = f'mssql+pyodbc://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_SERVER"]}/{os.environ["DB_DATABASE"]}?driver=ODBC+Driver+18+for+SQL+Server'

engine = create_engine(connection_string)

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
