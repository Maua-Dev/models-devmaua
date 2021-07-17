from pydantic import BaseModel

from src.enum.roles import Roles

from src.models.professor import Professor
from src.models.disciplina import Disciplina


class ProfessorResponsavel(Professor, BaseModel):
    roles: list[Roles] = [Roles.Professor, Roles.ProfessorResponsavelDisciplina]
    disciplinaResponsavel: Disciplina