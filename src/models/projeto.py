from pydantic import BaseModel, validator, root_validator
from datetime import time, date, datetime
from typing import Optional

from src.enum.areas import Areas
from src.enum.roles import Roles

from src.models.usuario import Usuario

class Projeto(BaseModel):
    nome: str
    area: Areas
    cargaHorariaSemanal: time
    professorOrientador: str #ID do professor orientador
    participantes: list[Usuario]
    inicioDoPrograma: date
    terminoDoPrograma: date
    descricao: Optional[str]
    encontros: list[datetime]
    
    @validator('nome')
    def nome_is_not_empty(cls, v):
        if len(v.replace(' ', '')) == 0 or v == None:
            raise ValueError('nome esta vazio')
        return v
    
    @validator('participantes', check_fields=False)
    def participantes_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('participantes is empty')
        return v
    
    @root_validator
    def profOrientador_in_participantes(cls, v):
        participantes = v.get('participantes')
        id_orientador = v.get('professorOrientador')
        for x in participantes:
            if Roles.Professor in x.roles:
                if x.ID == id_orientador:
                    return v
        raise ValueError('orientador not in participantes')
    
    def getProfessores(self):
        profs = []
        for x in self.participantes:
            if Roles.Professor in x.roles:
                profs.append(x)
        return profs
    
    def getAlunos(self):
        alunos = []
        for x in self.participantes:
            if Roles.Aluno in x.roles:
                alunos.append(x)
        return alunos
    
    def _area(self):
        return self.area.value.title()