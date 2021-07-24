from pydantic import BaseModel

from devmaua.src.enum.roles import Roles

from devmaua.src.models.aluno import Aluno
from devmaua.src.models.monitoria import Monitoria

class AlunoMonitorDisciplina(Aluno, BaseModel):
    monitoria: Monitoria
    roles: list[Roles] = [Roles.ALUNO, Roles.MONITOR_DISCIPLINA]