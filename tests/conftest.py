from app.database import get_db_url, Base
from sqlalchemy.engine import create_engine
from app.config import get_settings
from copy import deepcopy
import pytest
from .setup import engine


@pytest.fixture(autouse=True, scope="session")
def drop_database_after_tests():
    settings = get_settings(_env_file=".env.test")
    cloned_settings = deepcopy(settings)
    cloned_settings.db_name = ''
    root_engine = create_engine(get_db_url(cloned_settings))

    db = root_engine.connect()
    db.execute('commit')
    db.execute(f'create database if not exists {settings.db_name}')
    Base.metadata.create_all(bind=engine)

    yield

    db.execute(f'drop database {settings.db_name}')
    db.close()
