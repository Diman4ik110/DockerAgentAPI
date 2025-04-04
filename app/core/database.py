from peewee import *
import datetime

# Определяем базу данных (SQLite в данном примере)
db = SqliteDatabase('database')

class BaseModel(Model):
    class Meta:
        database = db

class Host(BaseModel):
    # Поле с ID хоста
    ID = CharField()
    # Основное поле hostname
    hostname = CharField()
    # Основное поле IP Address
    IPAddress = CharField()
    class Meta:
        table_name = 'hosts'
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class Network(BaseModel):
    # Поле с ID сети
    ID = CharField()
    # Поле с именем сети
    name = CharField()
    # Поле с типом сети
    type = CharField()

    class Meta:
        table_name = 'networks'
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
class Container(BaseModel):
    # Поле с ID контейнера
    ID = CharField()
    # Поле с ID хоста
    hostID = IntegerField()
    # Поле с именем контейнера
    name = CharField()

    class Meta:
        table_name = 'containers'
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class ContMetrics(BaseModel):
    # Поле с ID контейнера
    contID = CharField()
    # Поле с загрузкой процессора
    loadCPU = IntegerField()
    # Поле с загрузкой оперативной памяти
    loadRAM = IntegerField()

    class Meta:
        table_name = 'containerMetrics'
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class NetworkConn(BaseModel):
    # Поле с ID контейнера
    containerID = CharField()
    # Поле с ID сети
    networkID = CharField()
    class Meta:
        table_name = 'netConnection'
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class Agent(BaseModel):
    # Поле с ID контейнера
    HostID = IntegerField()
    # Поле с UUID
    UUID = TextField()
    # Поле с ID сети
    Status = TextField()
    class Meta:
        table_name = 'netConnection'
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)