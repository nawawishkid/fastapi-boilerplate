"""
Application database.
"""

from app.config import get_settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

settings = get_settings()
Base = declarative_base()


def get_db_url() -> str:
    return f"mysql+pymysql://{settings.db_user}:{settings.db_password}@{settings.db_host}/{settings.db_name}?charset=utf8mb4"


engine = create_engine(get_db_url())
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
