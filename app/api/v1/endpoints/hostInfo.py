from fastapi import APIRouter, Body
from app.models.schema import hostInfo
from app.core.database import *
from app.core.utils import *
from typing import List

router = APIRouter(prefix="/hosts", tags=["DockerMapper"])

@router.post("/sendHostInfo/")
async def sendHostInfo(host: List[hostInfo] = Body(...), request: Request = None):
    # Добавляем в базу хосты с проверкой на наличие
    for h in host:
        if not Host.select().where((Host.hostname == h.hostname) & (Host.IPAddress == getIPFromRequest(request=request))).exists():
            host1 = Host.create(
                hostname=h.hostname,
                IPAddress=getIPFromRequest(request=request)
            )
            host1.save()
    db.close()
    return {"code": "success"}

@router.get("/getHostList/")
async def getHostList():
    query = Host.select()
    result = []
    for host in query:
        result.append({"hostID": host.ID, "hostname": host.hostname})
    return result