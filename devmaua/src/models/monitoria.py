from pydantic import BaseModel, validator
from datetime import time, date, datetime
from typing import Optional

from devmaua.src.models.disciplina import Disciplina
from devmaua.src.models.curso import Curso
from devmaua.src.models.ra import RA

class Monitoria(BaseModel):
    disciplina: Disciplina
    curso: Curso
    cargaHorariaSemanal: time
    professorOrientador: str #ID do professor orientador
    monitor: RA
    inicioDoPrograma: date
    terminoDoPrograma: date
    descricao: Optional[str]
    atendimentos: list[datetime]
    
    @validator('professorOrientador')
    def professorOrientador_is_not_empty(cls, v):
        if len(v.replace(' ', '')) == 0 or v == None:
            raise ValueError('ID do Professor Orientador esta vazio')
        return v
    
    def criarAtendimento(self, horario: datetime):
        self.atendimentos.append(horario)
    
    def alterarAtendimento(self, horarioARemover: datetime, horarioAAdicionar: datetime)  :
        self.atendimentos.remove(horarioARemover)  
        self.atendimentos.append(horarioAAdicionar)