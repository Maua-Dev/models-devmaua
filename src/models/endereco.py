from src.enum.tipo_endereco import TipoEndereco
from pydantic import BaseModel
from typing import Optional


class Endereco(BaseModel):
    logradouro: str
    numero: int
    complemento: Optional[str]
    tipo: TipoEndereco
