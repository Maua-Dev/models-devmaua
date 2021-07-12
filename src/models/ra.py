from pydantic import BaseModel, validator


class RA(BaseModel):
    ano: int
    numero: str
    digito: int
    
    @validator('ano')
    def ano_is_valid(cls, v):
        if v < 0 or v > 99:
            raise ValueError('Ano invalido')
        return v
    
    @validator('numero')
    def numero_is_valid(cls, v):
        if len(v) != 5:
            raise ValueError('Numero do RA invalido')
        return v
    
    @validator('digito')
    def digito_is_valid(cls, v):
        if v < 0 or v > 9:
            raise ValueError('Digito invalido')
        return v
    
    def toString(self):
        try:
            v = str.format("%i.%s-%i" % (self.ano, self.numero, self.digito))
            return v
        except TypeError as e:
            print(e)
            