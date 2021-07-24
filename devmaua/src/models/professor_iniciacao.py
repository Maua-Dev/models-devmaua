from pydantic import BaseModel

from devmaua.src.enum.roles import Roles

from devmaua.src.models.professor import Professor
from devmaua.src.models.projeto import Projeto


class ProfessorIniciacao(Professor, BaseModel):
    roles: list[Roles] = [Roles.PROFESSOR, Roles.PROFESSOR_IC]
    projetoIC: Projeto