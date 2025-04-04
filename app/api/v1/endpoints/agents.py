from fastapi import APIRouter, Body
from app.models.schema import agentData
from app.core.database import *
from uuid import uuid4

router = APIRouter(prefix="/agents", tags=["DockerMapper"])

@router.post("/registerAgent/")
async def registerAgent(agentData: agentData = Body(...)):
    # Проверку на дубликаты
    for agent in agentData:
        if not Agent.select().where(Agent.UUID == agent.uuid).exists():
            host = Agent.select().where(Agent.IPAddress == agent.IPAddress).first()
            agentUUID = uuid4().hex
            agentCreate = Agent.create(
                name=agent.name,
                hostID=host.id,
                UUID=agentUUID
            )
            agentCreate.save()
    return {"authToken": agentUUID}

@router.post("/checkRegistration/")
async def checkRegister(authToken: str):
    print(authToken)
    
    return {"code": "success"}