
"""Application database settings, loaded from environment variables / .env."""
 
from functools import lru_cache
 
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL
 
 
class DatabaseSettings(BaseSettings):
    """Database configuration. Override any field via `DB_<FIELD>` env vars."""
 
    model_config = SettingsConfigDict(
        env_prefix="DB_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
 
    host: str = "postgres"
    port: int = 5432
    name: str = "analyst_platform"
    user: str = "analyst_user"
    password: SecretStr  # required: no default credentials in source control
 
    echo: bool = False
    pool_size: int = Field(default=10, ge=1)
    max_overflow: int = Field(default=20, ge=0)
    pool_timeout: float = Field(default=30.0, gt=0)
    pool_recycle: int = Field(default=1800, gt=0)  # seconds
 
    @property
    def url(self) -> URL:
        """Build the URL safely (handles special characters in the password)."""
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.name,
        )
 
 
@lru_cache
def get_db_settings() -> DatabaseSettings:
    return DatabaseSettings()