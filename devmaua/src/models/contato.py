from devmaua.src.models.telefone import Telefone
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco

from pydantic import BaseModel, validator


class Contato(BaseModel):
    telefones: list[Telefone]
    emails: list[Email]
    enderecos: list[Endereco]

    @validator('telefones', check_fields=False)
    def telefones_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Telefone is empty')
        return v

    @validator('emails', check_fields=False)
    def emails_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Emails is empty')
        return v

    @validator('enderecos', check_fields=False)
    def endereco_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Endereco is empty')
        return v
