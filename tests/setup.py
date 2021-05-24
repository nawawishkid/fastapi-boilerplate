from fastapi.applications import FastAPI
from app.config import get_settings
from app.dependencies import get_db_session
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session, sessionmaker
from app.database import get_db_url
from fastapi.testclient import TestClient

settings = get_settings(_env_file=".env.test")
engine = create_engine(get_db_url(settings))
TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_test_db_session() -> Session:
    try:
        db: Session = TestSession()
        yield db
    finally:
        db.close()


def get_test_client(app: FastAPI) -> TestClient:
    app.dependency_overrides[get_db_session] = get_test_db_session

    return TestClient(app)
