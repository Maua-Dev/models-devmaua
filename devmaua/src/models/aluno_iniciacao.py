from pydantic import BaseModel

from devmaua.src.enum.roles import Roles

from devmaua.src.models.aluno import Aluno
from devmaua.src.models.projeto import Projeto

class AlunoIniciacao(Aluno, BaseModel):
    projeto: Projeto
    roles: list[Roles] = [Roles.Aluno, Roles.AlunoIC]