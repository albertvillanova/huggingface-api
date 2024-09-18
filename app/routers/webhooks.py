from typing import Optional, Union

from fastapi import APIRouter


router = APIRouter(
    prefix="/settings/webhooks",
    tags=["webhooks"],
)


@router.get("")
async def list_webhooks(
    token: Union[str, bool, None] = None,
):
    return {"token": token}


@router.post("")
async def create_webhook(
    url: str,
    watched: list[dict[str, str]],
    *,
    token: Union[str, bool, None] = None,
):
    return {"url": url, "watched": watched, "token": token}


@router.get("/{webhook_id}")
async def get_webhook(
    webhook_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {"webhook_id": webhook_id, "token": token}


@router.post("/{webhook_id}")
async def update_webhook(
    webhook_id: str,
    url: Optional[str] = None,
    watched: Optional[list[dict[str, str]]] = None,
    *,
    token: Union[str, bool, None] = None,
):
    return {"webhook_id": webhook_id, "url": url, "watched": watched, "token": token}


@router.delete("/{webhook_id}")
async def delete_webhook(
    webhook_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {"webhook_id": webhook_id, "token": token}


@router.post("/{webhook_id}/disable")
async def disable_webhook(
    webhook_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {"webhook_id": webhook_id, "token": token}


@router.post("/{webhook_id}/enable")
async def enable_webhook(
    webhook_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {"webhook_id": webhook_id, "token": token}
