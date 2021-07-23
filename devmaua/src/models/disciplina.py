from devmaua.src.enum.tipo_disciplina import TipoDisciplina
from devmaua.src.enum.semestralidade import Semestralidade
from devmaua.src.enum.codigo_disciplina import CodigoDisciplina

from devmaua.src.models.professor import Professor
from devmaua.src.models.aluno import Aluno
from devmaua.src.models.aula import Aula

from pydantic import BaseModel


class Disciplina(BaseModel):
    codigo: CodigoDisciplina
    tipo: TipoDisciplina
    semestralidade: Semestralidade
    profOrientador: Professor
    professores: list[Professor]
    alunosMatriculados: list[Aluno]
    aulas: list[Aula]
    ofereceDp: bool
    
    def nome(self):
        return self.codigo.value
