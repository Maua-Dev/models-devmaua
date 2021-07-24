from pydantic import BaseModel

from devmaua.src.enum.roles import Roles
from devmaua.src.enum.cargo_representante import CargoRepresentante
from devmaua.src.enum.grupos import Grupo

from devmaua.src.models.aluno import Aluno


class AlunoRepresentante(Aluno, BaseModel):
    roles: list[Roles] = [Roles.ALUNO, Roles.REPRESENTANTE]
    cargo: CargoRepresentante
    grupoResponsavel: Grupo