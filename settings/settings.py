import logging

from pydantic import Field, ValidationInfo, field_validator
from pydantic_settings import BaseSettings

from environment import EnvironmentName
from settings.log import LoggingSettings


class DatabaseSettings(BaseSettings):
    host: str = Field(alias="DATABASE_HOST", default="postgresql://localhost:5432")
    name: str = Field(alias="DATABASE_NAME", default="nolas")
    min_pool_size: int = Field(alias="DATABASE_MIN_POOL_SIZE", default=5)
    max_pool_size: int = Field(alias="DATABASE_MAX_POOL_SIZE", default=20)

    @property
    def async_host(self) -> str:
        """Return the host URL with async driver for SQLAlchemy async engine."""
        return self.host.replace("postgresql://", "postgresql+asyncpg://", 1)


class WorkerSettings(BaseSettings):
    num_workers: int = Field(alias="WORKERS_NUM", default=2)
    max_connections_per_provider: int = Field(alias="WORKER_MAX_CONNECTIONS_PER_PROVIDER", default=50)


class IMAPSettings(BaseSettings):
    timeout: int = Field(alias="IMAP_TIMEOUT", default=300)
    idle_timeout: int = Field(alias="IMAP_IDLE_TIMEOUT", default=1740)  # 29 minutes (RFC requirement)


class Settings(BaseSettings):
    environment: EnvironmentName = Field(alias="ENVIRONMENT")

    database: DatabaseSettings = Field(default_factory=DatabaseSettings)
    logging: LoggingSettings = Field(default_factory=LoggingSettings)
    worker: WorkerSettings = Field(default_factory=WorkerSettings)
    imap: IMAPSettings = Field(default_factory=IMAPSettings)

    @field_validator("environment", mode="before")
    def set_logging_level(cls, level: str, info: ValidationInfo) -> EnvironmentName:
        try:
            return EnvironmentName(level)
        except ValueError:
            logging.getLogger(__name__).warning(f"Invalid environment: {level}")
            return EnvironmentName.DEVELOPMENT
