from src.enum.periodo import Periodo
from src.enum.codigo_disciplina import CodigoDisciplina
from src.enum.nome_curso import NomeCurso

from src.models.usuario import Usuario
from src.models.ra import RA

from typing import Optional
from pydantic import BaseModel, root_validator


class Aluno(Usuario, BaseModel):
    ra: RA
    curso: NomeCurso
    serie: int
    disciplinas: list[CodigoDisciplina]
    periodo: Periodo
    listaDPs: Optional[list[CodigoDisciplina]]
    hasDP: bool

    @root_validator
    def serie_is_valid(cls, v):
        periodo = v.get('periodo')
        serie = v.get('serie')
        if (((serie < 1 or serie > 5) and (periodo == Periodo.Diurno)) or ((serie < 1 or serie > 6) and (periodo == Periodo.Noturno))):
            raise ValueError('Serie invalida')
        return v
    
    @root_validator
    def hasDP_is_valid(cls, v):
        hasDP = v.get('hasDP')
        listaDPs = v.get('listaDPs')
        if (len(listaDPs) > 0 and hasDP == False) or ((len(listaDPs) == 0 or listaDPs == None) and hasDP == True):
            raise ValueError('hasDP tem valor invalido')
        return v