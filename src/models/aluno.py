from typing import Optional
from src.models.pessoa import Pessoa

from pydantic import BaseModel

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