"""
This file consists of FastAPI application (router) dependencies.
See https://fastapi.tiangolo.com/tutorial/dependencies/
"""

from app.database import DBSession
from sqlalchemy.orm.session import Session


async def get_db_session() -> Session:
    try:
        db = DBSession()
        yield db
    finally:
        db.close()
