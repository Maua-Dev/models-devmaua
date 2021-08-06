from pydantic import BaseModel, validator, ValidationError
import re
import abc

from devmaua.src.enum.tipo_email import TipoEmail

from devmaua.src.models.erros.erro_email import ErroDadosEmailInvalidos


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
    
    @staticmethod
    def criarEmailPorDict(dicionario: dict):
        """ Instancia um email a partir de um dicionario do tipo:
        {
            "email":"teste@teste.com",
            "tipo":1,
            "prioridade":1
        }
        
        """
        try:
            return Email(email = dicionario['email'],
                         tipo = dicionario['tipo'],
                         prioridade = dicionario['prioridade'])
        except ValidationError:
            raise ErroDadosEmailInvalidos
        except KeyError:
            raise ErroDadosEmailInvalidos