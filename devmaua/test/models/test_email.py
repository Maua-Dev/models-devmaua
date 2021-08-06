import pytest
from pydantic import ValidationError

from devmaua.src.enum.tipo_email import TipoEmail

from devmaua.src.models.email import Email

class Test_Email():
    
    def test_create_instance_model(self):
        email = Email(email='teste@teste.com',
                      tipo=TipoEmail.PRIVADO,
                      prioridade = 1)
        assert email.email == 'teste@teste.com'
        assert email.tipo == TipoEmail.PRIVADO
        assert email.prioridade == 1
        
    def test_validator_error_email(self):
        with pytest.raises(ValidationError) as error_info:
            email = Email(email='teste@.teste.com',
                      tipo=TipoEmail.PRIVADO,
                      prioridade = 1)
            
    def test_criar_email_por_dict(self):
        d = {
                "email": "teste@teste.com",
                "tipo": 1,
                "prioridade": 1
            }
        
        email = Email.criarEmailPorDict(d)
        
        assert email.email == 'teste@teste.com'
        assert email.tipo == TipoEmail.PRIVADO
        assert email.prioridade == 1