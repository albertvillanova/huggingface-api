from typing import Optional, Union

from fastapi import APIRouter


router = APIRouter(
    # prefix="/user-access-requests",
    tags=["user-access-requests"],
)


@router.get("/{repo_type}s/{repo_id}/user-access-request/{status}")
async def list_user_access_requests(
    repo_id: str,
    status: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "status": status,
        "repo_type": repo_type,
        "token": token,
    }


@router.post("/{repo_type}s/{repo_id}/user-access-request/handle")
async def handle_user_access_request(
    repo_id: str,
    user_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
    status: Optional[str] = None,
    message: Optional[str] = None,
):
    return {
        "repo_id": repo_id,
        "user_id": user_id,
        "repo_type": repo_type,
        "token": token,
        "status": status,
        "message": message,
    }


# TODO: Why /models/?
@router.post("/models/{repo_id}/user-access-request/grant")
async def grant_user_access(
    repo_id: str,
    user_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "user_id": user_id,
        "repo_type": repo_type,
        "token": token,
    }
