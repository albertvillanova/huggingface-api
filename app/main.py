from typing import Optional, Union

from fastapi import FastAPI

from .routers import collections
from .routers import datasets
from .routers import metrics
from .routers import models
from .routers import organizations
from .routers import repos
from .routers import spaces
from .routers import users

app = FastAPI()


@app.get("/{repo_type}s-tags-by-type")
async def list_repo_tags_by_type(
    repo_type: str,
):
    return {"repo_type": repo_type}


@app.post("/{repo_type}s/{repo_id}/like")
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


@app.delete("/{repo_type}s/{repo_id}/like")
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


@app.get("{repo_type}s/{repo_id}/likers")
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


@app.get("/{repo_type}s/{repo_id}")
async def read_repo(
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


@app.post("/{repo_type}s/{repo_id}/paths-info/{revision}")
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


@app.post("/{repo_type}s/{repo_id}/super-squash/{branch}")
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


@app.put("/{repo_type}s/{repo_id}/settings")
async def update_repo_settings(
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


@app.post("/{repo_type}s/{repo_id}/commit/{revision}")
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


@app.post("/{repo_type}s/{repo_id}/branch/{branch}")
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


@app.delete("/{repo_type}s/{repo_id}/branch/{branch}")
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


@app.post("/{repo_type}s/{repo_id}/tag/{revision}")
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


@app.delete("/{repo_type}s/{repo_id}/tag/{tag}")
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


@app.get("/{repo_type}s/{repo_id}/discussions")
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


@app.post("/{repo_type}s/{repo_id}/discussions")
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


@app.get("/{repo_type}s/{repo_id}/discussions/{discussion_num}")
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


@app.post("/{repo_type}s/{repo_id}/discussions/{discussion_num}/{resource}")
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


@app.post("/validate-yaml")
async def validate_yaml(
    content: str,
    *,
    repo_type: Optional[str] = None,
    token: Union[str, bool, None] = None,
):
    return {
        "content": content,
        "repo_type": repo_type,
        "token": token,
    }


@app.get("/{repo_type}s/{repo_id}/auth-check")
async def check_repo_auth(
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


app.include_router(users.router)
app.include_router(organizations.router)
app.include_router(repos.router)
app.include_router(models.router)
app.include_router(datasets.router)
app.include_router(spaces.router)
app.include_router(metrics.router)
app.include_router(collections.router)
