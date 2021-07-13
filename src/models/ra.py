import re

from pydantic import BaseModel, validator


class RA(BaseModel):
    ano: str
    numero: str
    digito: str
    
    @validator('ano')
    def ano_is_valid(cls, v):
        padrao = re.compile(r'[0-9]{2}$')
        valido = padrao.match(v)
        is_valid = bool(valido)
        if is_valid != True:
            raise ValueError('Ano invalido')
        return v
    
    @validator('numero')
    def numero_is_valid(cls, v):
        padrao = re.compile(r'[0-9]{5}$')
        valido = padrao.match(v)
        is_valid = bool(valido)
        if is_valid != True:
            raise ValueError('Numero do RA invalido')
        return v
    
    @validator('digito')
    def digito_is_valid(cls, v):
        padrao = re.compile(r'[0-9]{1}$')
        valido = padrao.match(v)
        is_valid = bool(valido)
        if is_valid != True:
            raise ValueError('Digito invalido')
        return v
    
    def toString(self):
        try:
            v = f"{self.ano}.{self.numero}-{self.digito}"
            return v
        except TypeError as e:
            print(e)
            