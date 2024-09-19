from typing import Annotated, Union

from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials

from ..dependencies import security


router = APIRouter(
    # prefix="/users",
    tags=["users"],
)


@router.get("/whoami-v2")
async def whoami(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
):
    token = credentials.credentials if credentials else None
    return {"token": token}


@router.get("/users/{user_id}/overview")
async def get_user_overview(
    user_id: str,
    token: Union[str, bool, None] = None,
):
    return {"user_id": user_id, "token": token}


@router.get("/users/{user_id}/likes")
async def list_user_likes(
    user_id: str,
    token: Union[str, bool, None] = None,
):
    return {"user_id": user_id, "token": token}


@router.get("/users/{user_id}/followers")
async def list_user_followers(
    user_id: str,
    token: Union[str, bool, None] = None,
):
    return {"user_id": user_id, "token": token}


@router.get("/users/{user_id}/following")
async def list_user_following(
    user_id: str,
    token: Union[str, bool, None] = None,
):
    return {"user_id": user_id, "token": token}
