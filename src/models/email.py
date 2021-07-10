from pydantic import BaseModel

class Email(BaseModel):
    email: str
    tipo: TipoEmail
    prioridade: int