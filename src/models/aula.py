from pydantic import BaseModel
from datetime import datetime, time, timedelta

from src.enum.codigo_disciplina import CodigoDisciplina

from src.models.sala import Sala
from src.models.professor import Professor


class Aula(BaseModel):
    disciplina: CodigoDisciplina
    local: Sala
    horario: datetime
    duracao: time
    professor: Professor

    def termino(self):
        termino = self.horario + timedelta(hours=self.duracao.hour, minutes=self.duracao.minute)
        return str(termino)