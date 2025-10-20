import logging
import sys
from contextlib import asynccontextmanager
from typing import cast

import structlog
from fastapi import FastAPI
from structlog.stdlib import BoundLogger

from .config import config

logger: BoundLogger = structlog.stdlib.get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.debug(f"Setting up the application '{app.title}'")

    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(
            cast(int, getattr(logging, config.log_level.upper()))
        ),
        cache_logger_on_first_use="pytest" not in sys.modules,
    )

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root() -> dict[str, str]:
    logger.info("Hello World")
    return {"message": "Hello World"}


@app.get("/sum/{a}/{b}")
async def sum(a: int, b: int) -> dict[str, int]:
    return {"result": a + b}
