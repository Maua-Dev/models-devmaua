import enum

class TipoAtividade(enum.Enum):
    MOODLE = 'Moodle'
    ATIVIDADE_DE_SALA = 'Atividade em Sala'
    PROVA = 'Prova'
    TRABALHO_SEMESTRAL = 'Trabalho Semestral'
    TRABALHO_EM_GRUPO = 'Trabalho em Grupo'
    KAHOOT = 'Kahoot'