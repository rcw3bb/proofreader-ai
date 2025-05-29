"""
model module for inference response.

Author: Ron Webb
Since: 1.0.0
"""

from collections.abc import Sequence
from typing import Any
from pydantic import BaseModel


class Message(BaseModel):
    """
    Pydantic model for the message field in the inference response.
    """

    content: str
    role: str
    annotations: Sequence[dict] = ()
    refusal: str | None = None


class ProofreadRequest(BaseModel):
    """
    Request model for the proofread endpoint.
    """

    model: str = "openai/gpt-4.1"
    text: str
    params: dict[str, Any] = {}


class ProofreadResponse(BaseModel):
    """
    Response model for the proofread endpoint.
    """

    messages: list[Message]
