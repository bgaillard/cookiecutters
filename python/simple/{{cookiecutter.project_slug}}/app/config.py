from functools import lru_cache
from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


# @see https://docs.pydantic.dev/latest/concepts/pydantic_settings/
class Config(BaseSettings):
    # The level of logging to use.
    log_level: str = "INFO"

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        # Each env file will be loaded in order, with each file overriding the previous one.
        #
        # Environment variables will always take priority over values loaded from a dotenv file.
        #
        # @see https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support
        env_file=(".env.local", ".env.test", ".env")
    )


@lru_cache
def get_config() -> Config:
    """Get the configuration of the application."""
    return Config()


config = get_config()
