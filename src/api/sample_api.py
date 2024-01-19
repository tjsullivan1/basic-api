import fastapi

from services import sample_service

router = fastapi.APIRouter()


@router.get("/api/v1/hello", tags=["sample"])
async def hello_world():
    return await sample_service.hello()


@router.get("/api/v1/hello/{name}", tags=["sample"])
async def hello_name(name: str):
    return await sample_service.hello(name)
