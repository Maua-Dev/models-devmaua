from src.models.disciplina import Disciplina
from src.models.pessoa import Pessoa

from pydantic import BaseModel

class Professor(Pessoa, BaseModel):
    _id: str
    disciplinas: list[Disciplina]
        