"""
message model for inference response.

Author: Ron Webb
Since: 1.0.0
"""

from collections.abc import Sequence
from pydantic import BaseModel


class MessageModel(BaseModel):
    """
    Pydantic model for the message field in the inference response.
    """

    content: str
    role: str
    annotations: Sequence[dict] = ()
    refusal: str | None = None
