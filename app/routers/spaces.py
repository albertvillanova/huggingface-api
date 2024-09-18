from typing import Union

from fastapi import APIRouter


router = APIRouter(
    prefix="/spaces",
    tags=["spaces"],
)


@router.get("")
async def list_spaces(
    token: Union[str, bool, None] = None,
):
    return {"token": token}


@router.post("/{repo_id}/secrets")
async def create_space_secret(
    repo_id: str,
    key: str,
    value: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
        "key": key,
        "value": value,
    }


@router.delete("/{repo_id}/secrets")
async def delete_space_secret(
    repo_id: str,
    key: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
        "key": key,
    }


@router.get("/{repo_id}/variables")
async def list_space_variables(
    repo_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
    }


@router.post("/{repo_id}/variables")
async def create_space_variable(
    repo_id: str,
    key: str,
    value: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
        "key": key,
        "value": value,
    }


@router.delete("/{repo_id}/variables")
async def delete_space_variable(
    repo_id: str,
    key: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
        "key": key,
    }


@router.get("/{repo_id}/runtime")
async def get_space_runtime(
    repo_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
    }


@router.post("/{repo_id}/hardware")
async def create_space_hardware(
    repo_id: str,
    hardware: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
        "hardware": hardware,
    }


@router.post("/{repo_id}/sleeptime")
async def set_space_sleep_time(
    repo_id: str,
    seconds: int,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
        "seconds": seconds,
    }


@router.post("/{repo_id}/pause")
async def pause_space(
    repo_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
    }


@router.post("/{repo_id}/restart")
async def restart_space(
    repo_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "repo_id": repo_id,
        "token": token,
    }

# TODO