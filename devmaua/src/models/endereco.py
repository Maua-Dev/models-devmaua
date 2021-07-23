import re
from pydantic import BaseModel, validator
from typing import Optional

from devmaua.src.enum.tipo_endereco import TipoEndereco



class Endereco(BaseModel):
    logradouro: str
    numero: int
    cep: str
    complemento: Optional[str]
    tipo: TipoEndereco

    @validator('numero')
    def numero_is_valid(cls, v):
        if v < 0:
            raise ValueError('numero invalido')
        return v
    
    @validator('cep')
    def cep_is_valid(cls, v):
        padrao = re.compile(r"[0-9]{5}\-[0-9]{3}$")
        valido = padrao.match(v)
        is_valid = bool(valido)
        if is_valid != True:
            raise ValueError('cep invalido')
        return v