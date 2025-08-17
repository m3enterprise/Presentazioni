from typing import Annotated, List
from fastapi import APIRouter, Body, HTTPException

from utils.available_models import list_available_bedrock_models

BEDROCK_ROUTER = APIRouter(prefix="/bedrock", tags=["Bedrock"])


@BEDROCK_ROUTER.post("/models/available", response_model=List[str])
async def get_available_models(
    access_key_id: Annotated[str, Body()],
    region: Annotated[str, Body()],
    secret_access_key: Annotated[str, Body()],
):
    try:
        return await list_available_bedrock_models(
            access_key=access_key_id,
            secret_key=secret_access_key,
            region=region,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
