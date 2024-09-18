from typing import Optional, Union

from fastapi import APIRouter


router = APIRouter(
    prefix="/models",
    tags=["models"],
)

@router.get("")
async def list_models(
    token: Union[str, bool, None] = None,
):
    return {"token": token}
