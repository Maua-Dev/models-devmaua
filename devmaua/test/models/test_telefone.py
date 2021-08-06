import pytest
from pydantic import ValidationError

from devmaua.src.enum.tipo_telefone import TipoTelefone

from devmaua.src.models.telefone import Telefone


class Test_Telefone():
    
    def test_create_instance_model(self):
        tel = Telefone(tipo = TipoTelefone.PRIVADO,
                       numero = '99999-9999',
                       ddd=11,
                       prioridade = 3)
        assert tel.tipo == TipoTelefone.PRIVADO
        assert tel.numero == "99999-9999"
        assert tel.prioridade == 3
        
    def test_validator_error_numero(self):
        with pytest.raises(ValidationError) as error_info:
            tel = Telefone(tipo = TipoTelefone.PRIVADO,
                       numero = '999999-9999',
                       ddd = 11,
                       prioridade = 3)
            
    def test_validator_error_ddd(self):
        with pytest.raises(ValidationError) as error_info:
            tel = Telefone(tipo = TipoTelefone.PRIVADO,
                       numero = '99999-9999',
                       ddd = 110,
                       prioridade = 3)
    
    def test_criar_telefone_por_dict(self):
        d = {
            "tipo":2,
            "numero":"99999-9999",
            "ddd":11,
            "prioridade":3
            }
        
        telefone = Telefone.criarTelefonePorDict(d)
        assert telefone.tipo == TipoTelefone.PRIVADO
        assert telefone.numero == "99999-9999"
        assert telefone.prioridade == 3
        
    