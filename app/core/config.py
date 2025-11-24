from pydantic_settings import BaseSettings
from functools import lru_cache
import os
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    """Application settings"""
    
    # App settings
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI Async Application")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("true", "1", "t")
    
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/dbname")
    
    # CORS settings  
    BACKEND_CORS_ORIGINS: list = os.getenv("BACKEND_CORS_ORIGINS", '["http://localhost:3000", "http://localhost:8000"]').strip("[]").replace('"', '').split(", ")
    
    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()


settings = get_settings()
