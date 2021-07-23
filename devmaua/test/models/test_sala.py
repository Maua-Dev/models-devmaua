import pytest
from pydantic import ValidationError

from devmaua.src.enum.tipo_sala import TipoSala
from devmaua.src.enum.campus import Campus

from devmaua.src.models.sala import Sala

class Test_Sala():
    
    def test_create_instance_model(self):
        sala = Sala(bloco='U',
                    numeroDaSala=22,
                    tipo=[TipoSala.Laboratorio],
                    campus = Campus.SCS)
        assert sala.bloco == 'U'
        assert sala.numeroDaSala == 22
        assert sala.tipo == [TipoSala.Laboratorio]
        assert sala.campus == Campus.SCS
        
    def test_validator_error_bloco(self):
        with pytest.raises(ValidationError) as error_info:
            sala = Sala(bloco='Z',
                        numeroDaSala=22,
                        tipo=[TipoSala.Laboratorio],
                        campus = Campus.SCS)
            
    def test_validator_error_numeroDaSala(self):
        with pytest.raises(ValidationError) as error_info:
            sala = Sala(bloco='U',
                        numeroDaSala=-22,
                        tipo=[TipoSala.Laboratorio],
                        campus = Campus.SCS)
            
    def test_validator_error_tipo(self):
        with pytest.raises(ValidationError) as error_info:
            sala = Sala(bloco='U',
                        numeroDaSala=22,
                        tipo=[],
                        campus = Campus.SCS)
        
    def test_validator_error_campusComBlocoInvalido(self):
        with pytest.raises(ValidationError) as error_info:
            sala = Sala(bloco='U',
                        numeroDaSala=22,
                        tipo=[TipoSala.Laboratorio],
                        campus = Campus.SP)    