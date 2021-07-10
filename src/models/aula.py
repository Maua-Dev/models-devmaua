from src.models.sala import Sala
from src.models.professor import Professor
from src.models.disciplina import Disciplina

from pydantic import BaseModel
from datetime import datetime, time

class Aula(BaseModel):
    disciplina: Disciplina
    local: Sala
    horario: datetime
    duracao: time
    professor: Professor