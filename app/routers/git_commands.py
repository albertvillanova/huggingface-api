from typing import Optional, Union

from fastapi import APIRouter


router = APIRouter(
    # prefix="/git-commands",
    tags=["git-commands"],
)


@router.get("/{repo_type}s/{repo_id}/commits/{revision}")
async def list_repo_commits(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[bool, str, None] = None,
    revision: Optional[str] = None,
    formatted: bool = False,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "token": token,
        "revision": revision,
        "formatted": formatted,
    }


@router.get("/{repo_type}s/{repo_id}/refs")
async def list_repo_refs(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    include_pull_requests: bool = False,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "include_pull_requests": include_pull_requests,
        "token": token,
    }


@router.get("/{repo_type}s/{repo_id}/tree/{revision}{path_in_repo}")
async def list_repo_tree(
    repo_id: str,
    path_in_repo: Optional[str] = None,
    *,
    recursive: bool = False,
    expand: bool = False,
    revision: Optional[str] = None,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "path_in_repo": path_in_repo,
        "recursive": recursive,
        "expand": expand,
        "revision": revision,
        "repo_type": repo_type,
        "token": token,
    }


@router.post("/{repo_type}s/{repo_id}/paths-info/{revision}")
async def list_repo_paths_info(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    revision: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "revision": revision,
        "token": token,
    }


@router.post("/{repo_type}s/{repo_id}/super-squash/{branch}")
async def super_squash(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    branch: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "branch": branch,
        "token": token,
    }


@router.post("/{repo_type}s/{repo_id}/commit/{revision}")
async def commit_repo(
    repo_id: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
    revision: Optional[str] = None,
    message: Optional[str] = None,
    description: Optional[str] = None,
    create_pr: Optional[bool] = None,
):
    return {
        "repo_id": repo_id,
        "repo_type": repo_type,
        "token": token,
        "revision": revision,
        "message": message,
        "description": description,
        "create_pr": create_pr,
    }


@router.post("/{repo_type}s/{repo_id}/branch/{branch}")
async def create_branch(
    repo_id: str,
    branch: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
    exist_ok: bool = False,
):
    return {
        "repo_id": repo_id,
        "branch": branch,
        "repo_type": repo_type,
        "token": token,
        "exist_ok": exist_ok,
    }


@router.delete("/{repo_type}s/{repo_id}/branch/{branch}")
async def delete_branch(
    repo_id: str,
    branch: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
    # missing_ok: bool = False,
):
    return {
        "repo_id": repo_id,
        "branch": branch,
        "repo_type": repo_type,
        "token": token,
        # "missing_ok": missing_ok,
    }


@router.post("/{repo_type}s/{repo_id}/tag/{revision}")
async def create_tag(
    repo_id: str,
    revision: str,
    tag: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "revision": revision,
        "repo_type": repo_type,
        "token": token,
        "tag": tag,
    }


@router.delete("/{repo_type}s/{repo_id}/tag/{tag}")
async def delete_tag(
    repo_id: str,
    tag: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "tag": tag,
        "repo_type": repo_type,
        "token": token,
    }
