from fastapi import APIRouter, Body, Request
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
                image=container.image,
                name=container.name,
                hostID=host.id
            )
            cont.save()
    return {"code": "success"}

@router.post("/sendContainerStats/")
async def sendMetrics(metrics: List[contMetrics] = Body(...)):
    for stat in metrics:
        cont = ContMetrics.create(
            contID=stat.contID,
            lastUpdate=stat.lastUpdate,
            loadRAM=stat.loadRAM,
            loadCPU=stat.loadCPU,
            status=stat.status
        )
        cont.save()
    return {"code": "success"}

@router.get("/getContList/")
async def getContList():
    query = Container.select()
    result = []
    for container in query:
        result.append({"contID": container.ID, "image": container.image, "name": container.name, "hostID": container.hostID})
    return result

@router.get("/getContView/")
async def getContView():
    query = ContView.select()
    result = []
    for container in query:
        result.append({"contID": container.ContID,
                       "status": container.status,
                       "ContName": container.ContName,
                       "HostID": container.HostID,
                       "hostname": container.hostname})
    return result