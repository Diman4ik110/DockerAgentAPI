from fastapi import APIRouter, Body
from app.models.schema import hostInfo
from app.core.database import *
from typing import List

router = APIRouter(prefix="/hosts", tags=["DockerMapper"])

@router.post("/sendHostInfo/")
async def sendHostInfo(host: List[hostInfo] = Body(...)):
    # Добавляем в базу хосты с проверкой на наличие
    for h in host:
        if not Host.select().where(Host.hostname == h.hostname).exists():
            host1 = Host.create(
                hostname=h.hostname,
            )
            host1.save()
    db.close()
    return {"code": "success"}

@router.get("/getHostList/")
async def getHostList():
    query = Host.select()
    result = []
    for host in query:
        result.append({"hostID": host.ID, "gostname": host.hostname})
    return result