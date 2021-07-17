from pydantic import BaseModel, validator

from src.enum.cargo import Cargo
from src.enum.setor import Setor
from src.enum.campus import Campus
from src.enum.roles import Roles

from src.models.usuario import Usuario

class Administrativo(Usuario, BaseModel):
    ID: str
    cargo: Cargo
    setor: Setor
    campus: Campus
    roles: list[Roles] = [Roles.Administrativo]
    
    @validator('ID')
    def ID_is_not_empty(cls, v):
        if len(v.replace(' ', '')) == 0 or v == None:
            raise ValueError('ID esta vazio')
        return v
    
    def _cargo(self):
        return self.cargo.value.title()
    
    def _setor(self):
        return self.setor.value.title()
    
    def _campus(self):
        return self.campus.value.title()