from src.enum.periodo import Periodo

from src.models.usuario import Usuario
from src.models.curso import Curso
from src.models.disciplina import Disciplina
from src.models.ra import RA

from typing import Optional
from pydantic import BaseModel, validator


class Aluno(Usuario, BaseModel):
    ra: RA
    curso: Curso
    serie: int
    disciplinas: list[Disciplina]
    periodo: Periodo
    listaDPs: Optional[list[Disciplina]]
    hasDP: bool

    @validator('ra')
    def ra_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('RA is empty')
        return v.title()
