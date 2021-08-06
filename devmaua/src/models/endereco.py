import re
from pydantic import BaseModel, validator, ValidationError
from typing import Optional
import abc

from devmaua.src.enum.tipo_endereco import TipoEndereco

from devmaua.src.models.erros.erro_endereco import ErroDadosEnderecoInvalidos


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
    
    @staticmethod
    def criarEnderecoPorDict(dicionario: dict):
        """ Instancia um endereco a partir de um dicionario do tipo:
        {
            "logradouro": "rua de tal",
            "numero": 20,
            "cep": "00000-000",
            "complemento": None,
            "tipo": 1
        }
        
        """
        
        try:
            return Endereco(logradouro = dicionario['logradouro'],
                            numero = dicionario['numero'],
                            cep = dicionario['cep'],
                            complemento = dicionario['complemento'],
                            tipo = dicionario['tipo'])
        
        except ValidationError:
            raise ErroDadosEnderecoInvalidos
        except KeyError:
            raise ErroDadosEnderecoInvalidos