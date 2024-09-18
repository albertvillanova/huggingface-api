from typing import Optional, Union

from fastapi import APIRouter


router = APIRouter(
    prefix="/collections",
    tags=["collections"],
)


@router.get("")
async def list_collections(
    token: Union[str, bool, None] = None,
):
    return {"token": token}


@router.post("")
async def create_collection(
    title: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {"title": title, "token": token}


@router.get("/{collection_id}")
async def get_collection(
    collection_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {"collection_id": collection_id, "token": token}


@router.patch("/{collection_id}")
async def update_collection(
    collection_id: str,
    *,
    token: Union[str, bool, None] = None,
    title: Optional[str] = None,
):
    return {"collection_id": collection_id, "title": title, "token": token}


@router.delete("/{collection_id}")
async def delete_collection(
    collection_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {"collection_id": collection_id, "token": token}


@router.post("/{collection_id}/items")
async def create_collection_item(
    collection_id: str,
    item_id: str,
    item_type: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "collection_id": collection_id,
        "item_id": item_id,
        "item_type": item_type,
        "token": token,
    }

@router.patch("/{collection_id}/items/{item_id}")
async def update_collection_item(
    collection_id: str,
    item_id: str,
    *,
    token: Union[str, bool, None] = None,
    item_type: Optional[str] = None,
):
    return {
        "collection_id": collection_id,
        "item_id": item_id,
        "item_type": item_type,
        "token": token,
    }

@router.delete("/{collection_id}/items/{item_id}")
async def delete_collection_item(
    collection_id: str,
    item_id: str,
    *,
    token: Union[str, bool, None] = None,
):
    return {
        "collection_id": collection_id,
        "item_id": item_id,
        "token": token,
    }
