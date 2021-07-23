import pytest
from pydantic import ValidationError

from devmaua.src.enum.tipo_endereco import TipoEndereco

from devmaua.src.models.endereco import Endereco

class Test_Endereco():
    
    def test_create_instance_model(self):
        end = Endereco(logradouro='rua de tal',
                       numero = 20,
                       cep='00000-000',
                       tipo = TipoEndereco.Residencial)
        assert end.logradouro == 'rua de tal'
        assert end.numero == 20
        assert end.cep == '00000-000'
        assert end.tipo == TipoEndereco.Residencial
        
    def test_validator_error_numero(self):
        with pytest.raises(ValidationError) as error_info:
            end = Endereco(logradouro='rua de tal',
                       numero = -20,
                       cep='00000-000',
                       tipo = TipoEndereco.Residencial)
            
    def test_validator_error_cep(self):
        with pytest.raises(ValidationError) as error_info:
            end = Endereco(logradouro='rua de tal',
                       numero = 20,
                       cep='a',
                       tipo = TipoEndereco.Residencial)