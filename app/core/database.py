from peewee import *

# Определяем базу данных (SQLite в данном примере)
db = SqliteDatabase('database.db')

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
    # Поле с названием образа
    image = CharField()
    class Meta:
        table_name = 'containers'
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class ContMetrics(BaseModel):
    # Поле с ID контейнера
    contID = CharField()
    # Поле с загрузкой процессора
    loadCPU = FloatField()
    # Поле с загрузкой оперативной памяти
    loadRAM = FloatField()

    status = CharField()

    lastUpdate = CharField()
    class Meta:
        table_name = 'containerStats'
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class NetworkConn(BaseModel):
    # Поле с ID контейнера
    containerID = CharField()
    # Поле с ID сети
    networkID = CharField()
    class Meta:
        table_name = 'netConnection'
        primary_key = False
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
        table_name = 'agents'
        primary_key = False
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class ContView(BaseModel):
    # Поле с ID контейнера
    ContID = CharField()
    # Поле с UUID
    status = IntegerField()
    # Поле с ID сети
    ContName = CharField()

    HostID = IntegerField()

    hostname = CharField()
    class Meta:
        table_name = 'containerView'
        primary_key = False
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    
class ConnView(BaseModel):
    # Поле с ID контейнера
    sourceID = CharField()
    # Поле с ID сети
    targetID = CharField()

    netID = CharField()
    class Meta:
        table_name = 'linksView'
        primary_key = False
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)