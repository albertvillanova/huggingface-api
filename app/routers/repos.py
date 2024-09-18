from typing import Optional, Union

from fastapi import APIRouter


router = APIRouter(
    prefix="/repos",
    tags=["repos"],
)


@router.post("/create")
async def create_repo(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
    exist_ok: bool = False,
    private: bool = False,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "token": token,
        "exist_ok": exist_ok,
        "private": private,
    }


@router.delete("/delete")
async def delete_repo(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
    missing_ok: bool = False,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "token": token,
        "missing_ok": missing_ok,
    }


@router.post("/move")
async def move_repo(
    from_repo_id: str,
    to_repo_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "from_repo_id": from_repo_id,
        "to_repo_id": to_repo_id,
        "repo_type": repo_type,
        "token": token,
    }
