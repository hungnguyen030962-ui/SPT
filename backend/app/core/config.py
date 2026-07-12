import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "SPT HNUE Exam Prep API"
    API_V1_STR: str = "/api"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./spt_prep.db")

    class Config:
        case_sensitive = True

settings = Settings()
