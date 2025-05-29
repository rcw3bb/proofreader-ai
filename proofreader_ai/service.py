"""
service module for GitHub Models inference API.

Author: Ron Webb
Since: 1.0.0
"""

import os
from typing import Any
import httpx
from dotenv import load_dotenv
from proofreader_ai.model import Message
from .logger import setup_logger


load_dotenv()
logger = setup_logger(__name__)

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
            logger.error("GitHub Models API token is required.")
            raise ValueError("GitHub Models API token is required.")

    async def run_inference(
        self, model: str, text: str, **params: Any
    ) -> list[Message]:
        """
        Run an inference request to proofread a text using the specified model.

        :param model: Model ID (e.g., 'openai/gpt-4.1').
        :param text: The text to be proofread.
        :param params: Additional parameters for the API.
        :return: List of Message containing the assistant's response messages.
        """
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
        }
        prompt = (
            "Proofread the following paragraph for grammar, spelling, and clarity. "
            "Output only the corrected text. Do not include explanations.\n\n"
            f"Paragraph: {text}"
        )
        messages = [
            {
                "role": "system",
                "content": "You are an expert proofreader. Always provide clear and concise corrections.",
            },
            {"role": "user", "content": prompt},
        ]
        payload = {"model": model, "messages": messages, **params}
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    GITHUB_API_URL, headers=headers, json=payload, timeout=30
                )
                response.raise_for_status()
                data = response.json()
                choices = data["choices"]
                logger.info("Inference successful for model '%s'", model)
                return [Message(**choice["message"]) for choice in choices]
        except Exception as exc:
            logger.error("Inference failed: %s", exc, exc_info=True)
            raise
