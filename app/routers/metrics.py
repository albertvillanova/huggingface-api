from typing import Union

from fastapi import APIRouter


router = APIRouter(
    prefix="/metrics",
    tags=["metrics"],
)


@router.get("")
async def list_metrics(
    token: Union[str, bool, None] = None,
):
    return {"token": token}
