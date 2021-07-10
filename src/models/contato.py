from src.models.telefone import Telefone

from pydantic import BaseModel, validator

class Contato(BaseModel):
    telefones: list[Telefone]
    emails: list[Email]
    endereco: list[Endereco]
    
    @validator('telefones')
    def telefones_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Telefone is empty')
        return v.title()
    
    @validator('emails')
    def emails_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Emails is empty')
        return v.title()
    
    @validator('Endereco')
    def endereco_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Endereco is empty')
        return v.title()