from pydantic import BaseModel

from src.enum.roles import Roles
from src.models.aluno import Aluno

class AlunoAdministrador(Aluno, BaseModel):
    roles: list[Roles] = [Roles.Aluno, Roles.Administrativo]