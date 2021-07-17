from pydantic import BaseModel

from src.enum.roles import Roles
from src.enum.cargo_representante import CargoRepresentante
from src.enum.grupos import Grupo

from src.models.aluno import Aluno


class AlunoRepresentante(Aluno, BaseModel):
    roles: list[Roles] = [Roles.Aluno, Roles.Representante]
    cargo: CargoRepresentante
    grupoResponsavel: Grupo