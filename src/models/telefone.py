import re

from src.enum.tipo_telefone import TipoTelefone

from pydantic import BaseModel, validator


class Telefone(BaseModel):
    tipo: TipoTelefone
    numero: str
    ddd: int
    prioridade: int

    @validator('numero')
    def numero_is_valid(cls, v):
        padrao = re.compile(r"[0-9]{4,5}\-[0-9]{4}$")
        valido = padrao.match(v)
        is_valid = bool(valido)
        if is_valid != True:
            raise ValueError('numero de telefone invalido')
        return v
    
    @validator('ddd')
    def ddd_is_valid(cls, v):
        ddd_valido = [11, 12 , 13, 14, 15, 16, 17, 18, 19, #SP
                      21, 22, 24, #RJ
                      27, 28, #ES
                      31, 32, 33, 34, 35, 37, 38, #MG
                      41, 42, 43, 44, 45, 46, #PR
                      47, 48, 49, #SC
                      51, 53, 54, 55, #RS
                      61, #DF
                      62, 64, #GO
                      63, #TO
                      65, 66, #MT
                      67, #MS
                      68, #AC
                      69, #RO
                      71,73,74,75,77, #BA
                      79, #SE
                      81, 87, #PE
                      82, #AL
                      83, #PB
                      84, #RN
                      85, 88, #CE
                      86, 89, #PI
                      91, 93, 94, #PA
                      92, 97, #AM
                      95, #RR
                      96, #AP
                      98, 99 #MA
                      ]
        if v not in ddd_valido:
            raise ValueError('ddd invalido')
        return v