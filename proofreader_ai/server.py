"""
server module for FastAPI application exposing the proofreader endpoint.

Author: Ron Webb
Since: 1.0.0
"""

from fastapi import FastAPI
from proofreader_ai.controller import router

app = FastAPI(
    title="Proofreader AI API",
    version="1.0.0",
    description="""
    Proofreader AI is an API-driven service for advanced proofreading using AI. 
    Submit your text to the `/api/proofread` endpoint to receive grammar, spelling, and style suggestions.
    """,
    contact={
        "name": "Ron Webb",
        "email": "ron@ronella.xyz",
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)
app.include_router(router, prefix="/api/v1")
