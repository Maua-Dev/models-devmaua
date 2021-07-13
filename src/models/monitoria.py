from pydantic import BaseModel
from datetime import time, date, datetime
from typing import Optional

from src.models.disciplina import Disciplina
from src.models.curso import Curso
from src.models.ra import RA

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
    
    def criarAtendimento(self, horario: datetime):
        self.atendimentos.append(horario)
    
    def alterarAtendimento(self, horarioARemover: datetime, horarioAAdicionar: datetime)  :
        self.atendimentos.remove(horarioARemover)  
        self.atendimentos.append(horarioAAdicionar)