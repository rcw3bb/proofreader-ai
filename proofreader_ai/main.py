"""
Main script to test InferenceService.

Author: Ron Webb
Since: 1.0.0
"""

import asyncio
from collections.abc import Sequence, Mapping
from proofreader_ai.service import InferenceService


async def main() -> None:
    """
    Run a sample inference request using InferenceService.
    """
    service = InferenceService()
    messages: Sequence[Mapping[str, str]] = [
        {"role": "user", "content": "Say hello in French."}
    ]
    try:
        response = await service.run_inference("openai/gpt-4.1", messages)
        print("Response:", response.model_dump())
    except Exception as exc:  # pylint: disable=broad-exception-caught
        print(f"Error: {exc}")


if __name__ == "__main__":
    asyncio.run(main())
