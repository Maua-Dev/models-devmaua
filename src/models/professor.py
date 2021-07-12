from src.enum.codigo_disciplina import CodigoDisciplina
from src.enum.tronco import Tronco
from src.enum.nome_curso import NomeCurso

from src.models.disciplina import Disciplina
from src.models.usuario import Usuario

from pydantic import BaseModel


class Professor(Usuario, BaseModel):
    ID: str
    troncos: list[Tronco]
    cursos: list[NomeCurso]
    disciplinas: list[CodigoDisciplina]
    
