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


@router.get("/{repo_id}")
async def get_dataset_info(
    repo_id: str,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
    }


@router.get("/{repo_id}/revision/{revision}")
async def get_dataset_info_at_revision(
    repo_id: str,
    revision: str,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "revision": revision,
        "token": token,
    }
