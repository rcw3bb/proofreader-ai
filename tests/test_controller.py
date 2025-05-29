"""
Test module for controller.

Author: Ron Webb
Since: 1.0.0
"""


import pytest
from httpx import AsyncClient
from fastapi import status
from proofreader_ai.server import app

@pytest.mark.asyncio
async def test_proofread_endpoint(monkeypatch):
    from proofreader_ai.model import Message
    async def dummy_run_inference(self, model, text, **params):
        return [Message(content="Corrected text.", role="assistant")]
    monkeypatch.setattr(
        "proofreader_ai.service.InferenceService.run_inference", dummy_run_inference
    )
    async with AsyncClient(base_url="http://test") as ac:
        from httpx import ASGITransport
        ac._transport = ASGITransport(app=app)
        response = await ac.post(
            "/api/v1/proofread",
            json={"model": "test-model", "text": "Ths is a tst.", "params": {}},
        )
    print("Response status:", response.status_code)
    print("Response content:", response.text)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "messages" in data
    assert data["messages"][0]["content"] == "Corrected text."
