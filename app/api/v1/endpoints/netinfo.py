from fastapi import APIRouter, Body
from app.models.schema import networkList, networkConnection
from app.core.database import *
from typing import List

router = APIRouter(prefix="/netinfo", tags=["DockerMapper"])

@router.post("/sendNetList/")
async def sendNetList(netList: List[networkList] = Body(...)):
    # Проверку на дубликаты
    for net in netList:
        if not Network.select().where(Network.ID == net.netID).exists():
            network = Network.create(
                ID=net.netID,
                name=net.name
            )
            network.save()
    return {"code": "success"}

@router.post("/sendNetConnection/")
async def sendNetConnection(netConnectList: List[networkConnection] = Body(...)):
    # Проверку на дубликаты
    for connect in netConnectList:
        if not NetworkConn.select().where((NetworkConn.networkID == connect.netID) & (NetworkConn.containerID == connect.contID)).exists():
            netConnect = NetworkConn.create(
                containerID=connect.contID,
                networkID=connect.netID
            )
            netConnect.save()
    return {"code": "success"}

@router.get("/getNetList/")
async def getNetList():
    query = Network.select()
    result = []
    for item in query:
        result.append({"netID": item.ID, "name": item.name})
    return result

@router.get("/getNetConnection/")
async def getNetConnection():
    query = NetworkConn.select()
    result = []
    for connection in query:
        result.append({"contID": connection.containerID, "netID": connection.networkID})
    return result

@router.get("/getLinksView/")
async def getLinksView():
    query = ConnView.select()
    result = []
    for container in query:
        result.append({"sourceID": container.sourceID,
                       "targetID": container.targetID,
                       "netID": container.netID,
                       })
    return result