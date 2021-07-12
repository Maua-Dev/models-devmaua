import pytest
from pydantic import ValidationError

from src.enum.tipo_telefone import TipoTelefone

from src.models.telefone import Telefone


class Test_Telefone():
    
    def test_create_instance_model(self):
        tel = Telefone(tipo = TipoTelefone.Privado,
                       numero = '99999-9999',
                       ddd=11,
                       prioridade = 3)
        assert tel.tipo == TipoTelefone.Privado
        assert tel.numero == "99999-9999"
        assert tel.prioridade == 3
        
    def test_validator_error_numero(self):
        with pytest.raises(ValidationError) as error_info:
            tel = Telefone(tipo = TipoTelefone.Privado,
                       numero = '999999-9999',
                       ddd = 11,
                       prioridade = 3)
            
    def test_validator_error_ddd(self):
        with pytest.raises(ValidationError) as error_info:
            tel = Telefone(tipo = TipoTelefone.Privado,
                       numero = '99999-9999',
                       ddd = 110,
                       prioridade = 3)
        
    