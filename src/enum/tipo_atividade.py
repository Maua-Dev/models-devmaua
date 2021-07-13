import enum

class TipoAtividade(enum.Enum):
    Moodle = 'Moodle'
    AtvSala = 'Atividade em Sala'
    Prova = 'Prova'
    TrabSemestral = 'Trabalho Semestral'
    TrabEmGrupo = 'Trabalho em Grupo'
    Kahoot = 'Kahoot'