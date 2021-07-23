from pydantic import BaseModel

from devmaua.src.enum.roles import Roles
from devmaua.src.models.aluno import Aluno

class AlunoAdministrador(Aluno, BaseModel):
    roles: list[Roles] = [Roles.Aluno, Roles.Administrativo]