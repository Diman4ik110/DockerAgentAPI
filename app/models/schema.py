from pydantic import BaseModel

# Класс который будет использоваться для валидации данных о виртуальных машинах
class hostInfo(BaseModel):
    hostname: str
    IPAddress: str

# Класс который будет использоваться для валидации данных о контейнерах
class contrainerInfo(BaseModel):
    name: str
    id: str
    hostname: str

# Класс который будет использоваться для валидации метрик
class contMetrics(BaseModel):
    contID: str
    loadCPU: int
    loadRAM: int

# Класс который будет использоваться для валидации данных о сетях к которым подключены контейнеры
class networkList(BaseModel):
    netID: str
    name: str

# Класс который будет использоваться для валидации данных о подключениях между контейнерами
class networkConnection(BaseModel):
    netID: str
    contID: str

# Класс который будет использоваться для валидации данных регистрации агентов
class agentData(BaseModel):
    token: str
    IPAddress: str

# Класс который будет использоваться для валидации токена агента
class agentData(BaseModel):
    token: str