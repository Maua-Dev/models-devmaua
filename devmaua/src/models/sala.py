from devmaua.src.enum.tipo_sala import TipoSala
from devmaua.src.enum.campus import Campus

from pydantic import BaseModel, validator, root_validator


class Sala(BaseModel):
    bloco: str
    numeroDaSala: int
    tipo: list[TipoSala]
    campus: Campus
    
    @root_validator
    def bloco_is_valid(cls, values):
        campus = values.get('campus')
        bloco = values.get('bloco').upper()
        if campus == Campus.SCS:
            blocos_validos = ['A', 'B', 'C', 'D', 'E', 'F',
                            'G', 'H', 'I', 'J', 'L', 'M',
                            'N', 'P', 'Q', 'R', 'S', 'U',
                            'V']
        if campus == Campus.SP:
            blocos_validos = [] #FAZER
        if bloco not in blocos_validos:
            raise ValueError('bloco invalido')
        values['bloco'] = values['bloco'].upper()
        return values
    
    @validator('numeroDaSala')
    def numero_is_valid(cls, v):
        if v < 1:
            raise ValueError('numero de sala invalido')
        return v
    
    @validator('tipo', check_fields=False)
    def tipo_is_empty(cls, v):
        if len(v) == 0:
            raise ValueError('tipo de sala is empty')
        return v