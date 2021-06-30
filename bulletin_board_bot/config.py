import logging
from enum import Enum
from typing import Optional

from pydantic import BaseSettings
from urlpath import URL

# Edit this!
PARSE_MODE = "HTML"


class UpdateMethod(str, Enum):
    WEBHOOKS = "webhooks"
    LONG_POLLING = "long_polling"


class LogLevel(int, Enum):
    CRITICAL = logging.CRITICAL
    FATAL = logging.FATAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    WARN = logging.WARN
    INFO = logging.INFO
    DEBUG = logging.DEBUG


class Config(BaseSettings):
    tg_token: str
    tg_admins_id: str
    tg_webhook_host: Optional[str]
    tg_webhook_path: str = "/bot"

    webapp_host: str = "localhost"
    webapp_port: int = 3000

    log_level: LogLevel = LogLevel.INFO
    log_format: str = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

    db_connection_str: str = "postgresql+asyncpg://localhost/bulletin_board_bot"

    @property
    def update_method(self) -> UpdateMethod:
        return UpdateMethod.LONG_POLLING if not self.tg_webhook_host else UpdateMethod.WEBHOOKS

    @property
    def tg_webhook_url(self) -> str:
        return str(URL(self.tg_webhook_host, self.tg_webhook_path))

    @property
    def parse_mode(self) -> str:
        # PARSE_MODE must be specified in the code, because the way
        # the message is parsed directly affects the code
        return PARSE_MODE


cfg = Config(
    _env_file=".env",
    _env_file_encoding="utf-8"
)
