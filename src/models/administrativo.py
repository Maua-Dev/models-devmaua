from pydantic import BaseModel, validator

from src.enum.cargo import Cargo
from src.enum.setor import Setor
from src.enum.campus import Campus


class Administrativo(BaseModel):
    ID: str
    cargo: Cargo
    setor: Setor
    campus: Campus
    
    @validator('ID')
    def ID_is_not_empty(cls, v):
        if len(v.replace(' ', '')) == 0 or v == None:
            raise ValueError('ID esta vazio')
        return v