from pydantic import BaseModel

from devmaua.src.enum.roles import Roles

from devmaua.src.models.professor import Professor


class Diretor(Professor, BaseModel):
    roles: list[Roles] = [Roles.Professor, Roles.ProfessorDiretor]