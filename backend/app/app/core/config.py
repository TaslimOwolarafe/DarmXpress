import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "DarmXpress"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///./darmxpress.db'

    class Config:
        env_file = 'env'

settings = Settings()