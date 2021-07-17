from pydantic import BaseModel

from src.enum.roles import Roles

from src.models.aluno import Aluno
from src.models.monitoria import Monitoria

class AlunoMonitorDisciplina(Aluno, BaseModel):
    monitoria: Monitoria
    roles: list[Roles] = [Roles.Aluno, Roles.MonitorDisciplina]