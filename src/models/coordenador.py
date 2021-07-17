from pydantic import BaseModel

from src.enum.roles import Roles

from src.models.professor import Professor
from src.models.curso import Curso


class Coordenador(Professor, BaseModel):
    roles: list[Roles] = [Roles.Professor, Roles.Coordenador]
    cursoCoordenado: Curso