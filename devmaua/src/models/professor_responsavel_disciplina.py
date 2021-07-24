from pydantic import BaseModel

from devmaua.src.enum.roles import Roles

from devmaua.src.models.professor import Professor
from devmaua.src.models.disciplina import Disciplina


class ProfessorResponsavel(Professor, BaseModel):
    roles: list[Roles] = [Roles.PROFESSOR, Roles.PROFESSOR_RESPONSAVEL_DISCIPLINA]
    disciplinaResponsavel: Disciplina