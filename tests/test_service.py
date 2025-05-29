"""
Test module for service.py.

Author: Ron Webb
Since: 1.0.0
"""

import pytest
import os
from collections.abc import Sequence, Mapping
from proofreader_ai.service import InferenceService

@pytest.mark.asyncio
async def test_run_inference_success(monkeypatch):
    """
    Test successful inference call with mocked response.
    """
    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return {"choices": [{"message": {"content": "Test response", "role": "assistant"}}]}

    class MockAsyncClient:
        async def __aenter__(self):
            return self
        async def __aexit__(self, exc_type, exc, tb):
            pass
        async def post(self, *args, **kwargs):
            return MockResponse()

    monkeypatch.setattr("httpx.AsyncClient", lambda: MockAsyncClient())
    service = InferenceService(token="dummy-token")
    text = "What is the capital of France?"
    result = await service.run_inference("openai/gpt-4.1", text)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].content == "Test response"

@pytest.mark.asyncio
async def test_run_inference_no_token(monkeypatch):
    """
    Test that ValueError is raised if no token is provided.
    """
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    # Remove the token from the environment for this test
    if "GITHUB_TOKEN" in os.environ:
        del os.environ["GITHUB_TOKEN"]
    with pytest.raises(ValueError):
        InferenceService(token=None)
