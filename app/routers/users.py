from typing import Optional, Union

from fastapi import APIRouter


router = APIRouter(
    # prefix="/users",
    tags=["users"],
)


@router.get("/whoami-v2")
async def whoami(
    token: Union[bool, str, None] = None,
):
    return {"token": token}


@router.get("/users/{user}/likes")
async def list_user_likes(
    user: str,
    token: Union[str, bool, None] = None,
):
    return {"user": user, "token": token}
