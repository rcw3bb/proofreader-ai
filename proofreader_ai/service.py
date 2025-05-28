"""
service module for GitHub Models inference API.

Author: Ron Webb
Since: 1.0.0
"""

import os
from collections.abc import Mapping, Sequence
from typing import Any
import httpx
from dotenv import load_dotenv
from proofreader_ai.message import MessageModel

load_dotenv()

GITHUB_API_URL = "https://models.github.ai/inference/chat/completions"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


class InferenceService:
    """
    Service for interacting with the GitHub Models inference API.
    """

    def __init__(self, token: str | None = None) -> None:
        """
        Initialize the inference service.

        :param token: GitHub Models API token. If None, uses environment variable.
        """
        env_token = os.getenv("GITHUB_TOKEN")
        self.token = token or env_token
        if not self.token:
            raise ValueError("GitHub Models API token is required.")

    async def run_inference(
        self, model: str, messages: Sequence[Mapping[str, Any]], **params: Any
    ) -> MessageModel:
        """
        Run an inference request using the specified model and messages.

        :param model: Model ID (e.g., 'openai/gpt-4.1').
        :param messages: List of message dicts as per API spec.
        :param params: Additional parameters for the API.
        :return: MessageModel containing the assistant's response message.
        """
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
        }
        payload = {"model": model, "messages": messages, **params}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                GITHUB_API_URL, headers=headers, json=payload, timeout=30
            )
            response.raise_for_status()
            data = response.json()
            # Extract the first message from choices
            message = data["choices"][0]["message"]
            return MessageModel(**message)
