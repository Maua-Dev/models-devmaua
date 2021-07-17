from pydantic import BaseModel

from src.enum.roles import Roles

from src.models.aluno import Aluno
from src.models.projeto import Projeto

class AlunoIniciacao(Aluno, BaseModel):
    projeto: Projeto
    roles: list[Roles] = [Roles.Aluno, Roles.AlunoIC]