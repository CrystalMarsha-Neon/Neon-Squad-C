from pydantic import BaseModel
from typing import List, Dict

class Postgres(BaseModel):
    host: str ='localhost'
    port: int = None
    username: str ='postgres'
    password: str ='admin'
    db: str ='postgres'

class Salt(BaseModel):
    salt: str = ''

class ConfigApps(BaseModel):
    ENVIRONMENT: str = ''
    APPS_INFORMATION: Dict = {}
    ALLOWED_HOSTS: List[str] = []
    ALLOW_METHODS: List[str]  = []
    API_TOKEN: List[str]  = []
    DATABASE: Postgres
    SALT: Salt