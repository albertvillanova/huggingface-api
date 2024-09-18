from typing import Optional, Union

from fastapi import APIRouter


router = APIRouter(
    prefix="/datasets",
    tags=["datasets"],
)

@router.get("")
async def list_datasets(
    token: Union[str, bool, None] = None,
):
    return {"token": token}