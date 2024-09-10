from typing import Optional, Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/{repo_type}s/{repo_id}/commits/{revision}")
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


@app.get("/{repo_type}s/{repo_id}/refs")
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


@app.get("/{repo_type}s/{repo_id}/tree/{revision}{path_in_repo}")
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
