from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import INTEGER, TEXT, VARCHAR
from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(INTEGER, primary_key=True, nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    password = Column(TEXT, nullable=False)
    name = Column(VARCHAR(255))
