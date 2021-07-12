from src.enum.tipo_disciplina import TipoDisciplina
from src.enum.semestralidade import Semestralidade
from src.enum.codigo_disciplina import CodigoDisciplina

from src.models.professor import Professor
from src.models.aluno import Aluno
from src.models.aula import Aula

from pydantic import BaseModel


class Disciplina(BaseModel):
    codigo: CodigoDisciplina
    tipo: TipoDisciplina
    semestralidade: Semestralidade
    profOrientador: Professor
    nome: str
    professores: list[Professor]
    alunosMatriculados: list[Aluno]
    aulas: list[Aula]
    ofereceDp: bool
