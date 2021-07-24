from pydantic import BaseModel

from devmaua.src.enum.roles import Roles

from devmaua.src.models.professor import Professor
from devmaua.src.models.curso import Curso


class Coordenador(Professor, BaseModel):
    roles: list[Roles] = [Roles.PROFESSOR, Roles.COORDENADOR]
    cursoCoordenado: Curso