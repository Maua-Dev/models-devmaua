from pydantic import BaseModel

from src.enum.roles import Roles

from src.models.professor import Professor
from src.models.projeto import Projeto


class ProfessorIniciacao(Professor, BaseModel):
    roles: list[Roles] = [Roles.Professor, Roles.ProfessorIC]
    projetoIC: Projeto