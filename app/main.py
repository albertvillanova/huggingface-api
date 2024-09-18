from typing import Optional, Union

from fastapi import FastAPI

from .routers import activity
from .routers import collections
from .routers import datasets
from .routers import git_commands
from .routers import metrics
from .routers import models
from .routers import organizations
from .routers import repos
from .routers import spaces
from .routers import tags
from .routers import users
from .routers import user_access
from .routers import webhooks

app = FastAPI()


# @app.get("/{repo_type}s-tags-by-type")
# async def list_repo_tags_by_type(
#     repo_type: str,
# ):
#     return {"repo_type": repo_type}


# @app.get("/{repo_type}s/{repo_id}")
# async def read_repo(
#     repo_id: str,
#     *,
#     repo_type: Optional[str] = None,
#     token: Union[str, bool, None] = None,
# ):
#     return {
#         "repo_id": repo_id,
#         "repo_type": repo_type,
#         "token": token,
#     }


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
# /{repo_type}s/
app.include_router(models.router)
app.include_router(datasets.router)
app.include_router(spaces.router)
app.include_router(git_commands.router)
app.include_router(activity.router)
app.include_router(user_access.router)
#
app.include_router(metrics.router)
app.include_router(tags.router)
app.include_router(collections.router)
app.include_router(webhooks.router)
