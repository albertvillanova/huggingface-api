from typing import Union

from fastapi import APIRouter


router = APIRouter(
    prefix="/organizations",
    tags=["organizations"],
)


@router.get("/{organization_id}/members")
async def list_organization_members(
    organization_id: str,
    token: Union[str, bool, None] = None,
):
    return {"organization_id": organization_id, "token": token}
