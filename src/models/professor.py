from src.models.disciplina import Disciplina
from src.models.usuario import Usuario

from pydantic import BaseModel


class Professor(Usuario, BaseModel):
    _id: str
    disciplinas: list[Disciplina]
