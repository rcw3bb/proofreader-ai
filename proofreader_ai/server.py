"""
server module for FastAPI application exposing the proofreader endpoint.

Author: Ron Webb
Since: 1.0.0
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from proofreader_ai.controller import router
from proofreader_ai.logger import setup_logger


logger = setup_logger(__name__)


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    """
    Lifespan context manager for FastAPI app startup and shutdown events.
    Logs the application name and version at server startup.
    Author: Ron Webb
    Since: 1.1.0
    """
    logger.info("Starting %s version %s", fastapi_app.title, fastapi_app.version)
    yield


app = FastAPI(
    title="Proofreader AI API",
    version="1.1.0",
    description="""
    Proofreader AI is an API-driven service for advanced proofreading using AI. 
    Submit your text to the `/api/v1/proofread` endpoint to receive grammar, spelling, and style suggestions.
    """,
    contact={
        "name": "Ron Webb",
        "email": "ron@ronella.xyz",
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.include_router(router, prefix="/api/v1")
