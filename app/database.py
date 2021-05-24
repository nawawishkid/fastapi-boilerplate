"""
Application database.
"""

from app.config import Settings, get_settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()


def get_db_url(settings: Settings) -> str:
    return f"mysql+pymysql://{settings.db_user}:{settings.db_password}@{settings.db_host}/{settings.db_name}?charset=utf8mb4"


engine = create_engine(get_db_url(get_settings()))
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
