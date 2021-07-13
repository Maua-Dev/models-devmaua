from pydantic import BaseModel
from datetime import datetime, time

from src.enum.codigo_disciplina import CodigoDisciplina

from src.models.sala import Sala
from src.models.professor import Professor


class Aula(BaseModel):
    disciplina: CodigoDisciplina
    local: Sala
    horario: datetime
    duracao: time
    professor: Professor
