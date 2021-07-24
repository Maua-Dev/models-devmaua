import enum

class StatusAvaliacao(enum.Enum):
    
    AVALIADO = 'Avaliado'
    ENVIADO = 'Enviado para avaliação'
    SEM_NOTAS = 'Não há notas'
    NAO_ENVIADO = 'Não enviado'