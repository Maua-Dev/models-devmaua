from src.enum.codigo_disciplina import CodigoDisciplina
from src.enum.tronco import Tronco
from src.enum.nome_curso import NomeCurso

from src.models.usuario import Usuario

from pydantic import BaseModel, validator


class Professor(Usuario, BaseModel):
    ID: str
    troncos: list[Tronco]
    cursos: list[NomeCurso]
    disciplinas: list[CodigoDisciplina]
    
    @validator('troncos', check_fields=False)
    def troncos_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('troncos is empty')
        return v
    
    @validator('cursos', check_fields=False)
    def cursos_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('cursos is empty')
        return v
    
    @validator('disciplinas', check_fields=False)
    def disciplinas_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('disciplinas is empty')
        return v