from src.enum.tipo_sala import TipoSala

from pydantic import BaseModel


class Sala(BaseModel):
    bloco: str
    numeroDaSala: str
    tipo: list[TipoSala]
