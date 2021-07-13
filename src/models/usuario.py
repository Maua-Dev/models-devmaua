from datetime import date, datetime
from pydantic import BaseModel, validator
import re

from src.enum.roles import Roles
from src.models.contato import Contato


class Usuario(BaseModel):
    nome: str
    contato: Contato
    nascimento: date
    roles: list[Roles]

    @validator('nome')
    def nome_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Nome is empty')
        return v.title()
    
    @validator('roles', check_fields=False)
    def roles_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('roles is empty')
        return v

    