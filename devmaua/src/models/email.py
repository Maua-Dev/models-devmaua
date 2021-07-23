from pydantic import BaseModel, validator
import re

from devmaua.src.enum.tipo_email import TipoEmail


class Email(BaseModel):
    email: str
    tipo: TipoEmail
    prioridade: int

    @validator('email')
    def email_is_valid(cls, v):
        padrao = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        valido = padrao.match(v)
        is_valid = bool(valido)
        if is_valid != True:
            raise ValueError('email invalido')
        return v