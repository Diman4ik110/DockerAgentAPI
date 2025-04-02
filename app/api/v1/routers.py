from fastapi import APIRouter
from .endpoints import metrics, vms

router = APIRouter()

router.include_router(router=metrics.router)
router.include_router(router=vms.router)