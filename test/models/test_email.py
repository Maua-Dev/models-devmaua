import pytest
from pydantic import ValidationError

from src.enum.tipo_email import TipoEmail

from src.models.email import Email

class Test_Email():
    
    def test_create_instance_model(self):
        email = Email(email='teste@teste.com',
                      tipo=TipoEmail.Privado,
                      prioridade = 1)
        assert email.email == 'teste@teste.com'
        assert email.tipo == TipoEmail.Privado
        assert email.prioridade == 1
        
    def test_validator_error_email(self):
        with pytest.raises(ValidationError) as error_info:
            email = Email(email='teste@.teste.com',
                      tipo=TipoEmail.Privado,
                      prioridade = 1)