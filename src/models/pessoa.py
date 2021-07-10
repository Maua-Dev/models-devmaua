from datetime import date
from pydantic import BaseModel, validator

class Pessoa(BaseModel):
    nome: str
    contato: Contato #fazer
    nascimento: date
    roles: list[Roles]

    @validator('nome')
    def nome_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Nome is empty')
        return v.title()