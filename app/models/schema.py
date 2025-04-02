from pydantic import BaseModel


# Класс который будет использоваться для валидации данных о виртуальных машинах
class VMMetrics(BaseModel):
    name: str
    cpu: int
    ram: int

# Класс который будет использоваться для валидации данных о контейнерах
class contrainermetrics(BaseModel):
    name: str
    id: str

# Класс который будет использоваться для валидации данных о сетях к которым подключены контейнеры
class networkData(BaseModel):
    name: str
    containers: list
