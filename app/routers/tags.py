from fastapi import APIRouter


router = APIRouter(
    # prefix="/tags",
    tags=["tags"],
)


@router.get("/models-tags-by-type")
async def list_models_tags():
    return {}


@router.get("/datasets-tags-by-type")
async def list_dataset_tags():
    return {}
