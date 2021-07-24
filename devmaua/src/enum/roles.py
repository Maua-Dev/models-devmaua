import enum


class Roles(enum.Enum):
    # Administrativo
    ADMINISTRATIVO = 1

    # Professor
    PROFESSOR = 2
    PROFESSOR_RESPONSAVEL_DISCIPLINA = 3
    COORDENADOR = 4
    PROFESSOR_IC = 5
    RESPONSAVEL_EVASAO = 6
    RESPONSAVEL_PESQUISA = 7
    PROFESSOR_DIRETOR = 8

    # Aluno
    ALUNO = 9
    RESPONSAVEL = 10
    ALUNO_POS = 11
    REPRESENTANTE = 12
    MONITOR_DISCIPLINA = 13
    MONITOR_PROJETO = 14
    ALUNO_IC = 15
