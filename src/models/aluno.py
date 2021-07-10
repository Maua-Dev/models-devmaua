from src.enum.periodo import Periodo

from src.models.pessoa import Pessoa
from src.models.curso import Curso
from src.models.disciplina import Disciplina

from typing import Optional
from pydantic import BaseModel, validator

class Aluno(Pessoa, BaseModel):
    ra: str
    curso: Curso
    serie: int
    disciplinas: list[Disciplina]
    periodo: Periodo
    hasDP: Optional[list[Disciplina]]
    
    @validator('ra')
    def ra_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('RA is empty')
        return v.title()