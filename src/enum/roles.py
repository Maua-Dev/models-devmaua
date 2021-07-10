import enum

class Roles(enum.Enum):
    # Administrativo
    Administratvo = 1
    
    # Professor
    Professor = 2
    ProfessorResponsavelDisciplina = 3
    Coordenador = 4
    ProfessorIC = 5
    ResponsavelEvasao = 6
    ResponsavelPesquisa = 7
    ProfessorDiretor = 8
    
    # Aluno
    Aluno = 9
    Responsavel = 10
    AlunoPos = 11
    Representante = 12
    MonitorDisciplina = 13
    MonitorProjeto = 14
    AlunoIC = 15