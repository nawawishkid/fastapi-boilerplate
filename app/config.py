"""
Application configuration.
"""

from enum import Enum
import logging
from typing import Optional
from pydantic import BaseSettings
from functools import lru_cache


class LogLevel(str, Enum):
    debug = 'DEBUG'
    info = 'INFO'
    warning = 'WARNING'
    error = 'ERROR'
    critical = 'CRITICAL'


class Env(str, Enum):
    dev = 'development'
    prod = 'production'
    test = 'test'


uvicorn_log_level = logging.getLevelName(
    logging.getLogger('uvicorn.error').getEffectiveLevel()).upper()


class Settings(BaseSettings):
    env: Optional[Env] = Env.prod
    log_level: Optional[LogLevel] = uvicorn_log_level
    db_host: str
    db_user: str
    db_password: str
    db_name: str

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()
