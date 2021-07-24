from devmaua.src.enum.periodo import Periodo
from devmaua.src.enum.tronco import Tronco
from devmaua.src.enum.nome_curso import NomeCurso

from devmaua.src.models.disciplina import Disciplina

from pydantic import BaseModel, root_validator


class Curso(BaseModel):
    tronco: Tronco
    disciplinas: list[Disciplina]
    periodo: Periodo
    nome: NomeCurso
    duracao: int
    
    def _nome(self):
        return self.nome.value.title()
    
    def _tronco(self):
        return self.tronco.value.title()
    
    def _periodo(self):
        return self.periodo.value

    @root_validator
    def duracao_is_valid(cls, v):
        periodo = v.get('periodo')
        duracao = v.get('duracao')
        if ((periodo == Periodo.DIURNO and (duracao<1 or duracao>5)) or (periodo == Periodo.NOTURNO and (duracao<1 or duracao>6))):
            raise ValueError('duracao invalida')
        return v