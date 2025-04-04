from fastapi import APIRouter
from .endpoints import agents, containers, hostInfo, netinfo

router = APIRouter()

router.include_router(router=containers.router)
router.include_router(router=hostInfo.router)
router.include_router(router=netinfo.router)
router.include_router(router=agents.router)