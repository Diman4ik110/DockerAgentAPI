from fastapi import APIRouter, Body
from app.models.schema import contrainerInfo, contMetrics
from app.core.database import *
from typing import List

router = APIRouter(prefix="/containers", tags=["DockerMapper"])

@router.post("/sendContList/")
async def sendContList(containers: List[contrainerInfo] = Body(...)):
    # Проверку на дубликаты
    for container in containers:
        if not Container.select().where(Container.ID == container.id).exists():
            host = Host.select().where(Host.hostname == container.hostname).first()
            cont = Container.create(
                ID=container.id,
                name=container.name,
                hostID=host.id
            )
            cont.save()
    return {"code": "success"}
@router.post("/sendMetrics/")
async def sendMetrics(metrics: List[contMetrics] = Body(...)):
    # Проверку на дубликаты
    for container in containers:
        if not ContMetrics.select().where(ContMetrics.ID == container.id).exists():
            host = Host.select().where(Host.hostname == container.hostname).first()
            cont = Container.create(
                ID=container.id,
                name=container.name,
                hostID=host.id
            )
            cont.save()
    return {"code": "success"}
@router.get("/getContList/")
async def getContList():
    query = Container.select()
    result = []
    for container in query:
        result.append({"contID": container.ID, "name": container.name, "hostID": container.hostID})
    return result