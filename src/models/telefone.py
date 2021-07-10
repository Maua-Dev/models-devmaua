from src.enum.tipo_telefone import TipoTelefone

from pydantic import BaseModel

class Telefone(BaseModel):
    tipo: TipoTelefone
    numero: str
    prioridade: int
    