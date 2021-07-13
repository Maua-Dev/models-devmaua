import enum

class StatusAvaliacao(enum.Enum):
    
    Avaliado = 'Avaliado'
    Enviado = 'Enviado para avaliação'
    SemNotas = 'Não há notas'
    NaoEnviado = 'Não enviado'