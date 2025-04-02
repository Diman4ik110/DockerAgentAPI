from fastapi import APIRouter
from app.models.schema import VMMetrics

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/sendMetrics/", response_model=VMMetrics)
async def create_user(user: VMMetrics):
    return await service.create_user(user)