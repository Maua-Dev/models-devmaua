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

    @validator('serie', 'periodo')
    def serie_is_valid(cls, v):
        periodo = v.get('periodo')
        serie = v.get('serie')
        if ((v < 1 and v > 5) and (periodo != Periodo.Diurno)) or ((v < 1 and v > 6) and (periodo != Periodo.Noturno)):
            raise ValueError('Serie invalida')
        return v
