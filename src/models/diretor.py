from pydantic import BaseModel

from src.enum.roles import Roles

from src.models.professor import Professor


class Diretor(Professor, BaseModel):
    roles: list[Roles] = [Roles.Professor, Roles.ProfessorDiretor]