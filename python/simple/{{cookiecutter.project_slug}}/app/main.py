import logging
import sys
import structlog
from typing import cast
from structlog.stdlib import BoundLogger

from .config import config

structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(
        cast(int, getattr(logging, config.log_level.upper()))
    ),
    cache_logger_on_first_use="pytest" not in sys.modules,
)

logger: BoundLogger = structlog.stdlib.get_logger(__name__)


def sum(a: int, b: int) -> int:
    return a + b


logger.info("Hello, world!")
