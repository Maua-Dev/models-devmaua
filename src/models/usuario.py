from datetime import date, datetime
from pydantic import BaseModel, validator
import re
from typing import Optional

from src.enum.roles import Roles
from src.models.contato import Contato


class Usuario(BaseModel):
    nome: str
    contato: Contato
    nascimento: date
    roles: list[Roles]
    timestamp: Optional[datetime]

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
    
    @validator('nascimento')
    # Assume-se que nenhum usuario da faculdade tem menos de 15 anos
    def year_is_valid(cls, v):
        if v.year > (datetime.now().year - 15):
            raise ValueError('ano invalido')
        return v