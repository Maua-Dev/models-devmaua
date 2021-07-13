from src.enum.periodo import Periodo
from src.enum.tronco import Tronco
from src.enum.nome_curso import NomeCurso

from src.models.disciplina import Disciplina

from pydantic import BaseModel, root_validator


class Curso(BaseModel):
    tronco: Tronco
    disciplinas: list[Disciplina]
    periodo: Periodo
    nome: NomeCurso
    duracao: int
    
    def nome(self):
        return self.nome.value.title()
    
    def tronco(self):
        return self.tronco.value.title()

    @root_validator
    def duracao_is_valid(cls, v):
        periodo = v.get('periodo')
        duracao = v.get('duracao')
        if ((periodo == Periodo.Diurno and (duracao<1 or duracao>5)) or (periodo == Periodo.Noturno and (duracao<1 or duracao>6))):
            raise ValueError('duracao invalida')
        return v