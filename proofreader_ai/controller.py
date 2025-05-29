"""
controller module for proofreader endpoint.

Author: Ron Webb
Since: 1.0.0
"""

from fastapi import APIRouter, HTTPException
from proofreader_ai.service import InferenceService
from proofreader_ai.model import ProofreadRequest, ProofreadResponse

router = APIRouter()


@router.post("/proofread", response_model=ProofreadResponse)
async def proofread(request: ProofreadRequest) -> ProofreadResponse:
    """
    Proofread endpoint using InferenceService.
    """
    service = InferenceService()
    try:
        messages = await service.run_inference(
            request.model, request.text, **request.params
        )
        return ProofreadResponse(messages=messages)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
