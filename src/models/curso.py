from src.enum.periodo import Periodo
from src.enum.tronco import Tronco
from src.enum.nome_curso import NomeCurso

from src.models.disciplina import Disciplina

from pydantic import BaseModel, validator


class Curso(BaseModel):
    tronco: Tronco
    disciplinas: list[Disciplina]
    periodo: Periodo
    nome: NomeCurso
    duracao: int
