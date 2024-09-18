from typing import Optional, Union

from fastapi import APIRouter


router = APIRouter(
    # prefix="/discussions",
    tags=["discussions"],
)


@router.get("/{repo_type}s/{repo_id}/discussions")
async def list_discussions(
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


@router.post("/{repo_type}s/{repo_id}/discussions")
async def create_discussion(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "token": token,
        "title": title,
        "description": description,
    }


@router.get("/{repo_type}s/{repo_id}/discussions/{discussion_num}")
async def get_discussion(
    repo_id: str,
    discussion_num: int,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "discussion_num": discussion_num,
        "repo_type": repo_type,
        "token": token,
    }


@router.post("/{repo_type}s/{repo_id}/discussions/{discussion_num}/{resource}")
async def update_discussion_resource(
    repo_id: str,
    discussion_num: int,
    resource: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "discussion_num": discussion_num,
        "resource": resource,
        "repo_type": repo_type,
        "token": token,
    }
