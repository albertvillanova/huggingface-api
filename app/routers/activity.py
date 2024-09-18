from typing import Optional, Union

from fastapi import APIRouter


router = APIRouter(
    # prefix="/activity",
    tags=["activity"],
)


@router.post("/{repo_type}s/{repo_id}/like")
async def like_repo(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "token": token,
    }


@router.delete("/{repo_type}s/{repo_id}/like")
async def unlike_repo(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "token": token,
    }


@router.get("/{repo_type}s/{repo_id}/likers")
async def list_repo_likers(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "token": token,
    }