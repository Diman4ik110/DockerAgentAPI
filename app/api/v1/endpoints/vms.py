from fastapi import APIRouter
from app.models.schema import VMMetrics

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/sendVmMetrics/", response_model=VMMetrics)
async def sendVMMetrics(user: VMMetrics):
    return {"code": "success"}