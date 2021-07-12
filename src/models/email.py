from src.enum.tipo_email import TipoEmail

from pydantic import BaseModel


class Email(BaseModel):
    email: str
    tipo: TipoEmail
    prioridade: int
