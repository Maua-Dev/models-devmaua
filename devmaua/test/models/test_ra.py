import pytest
from pydantic import ValidationError
from devmaua.src.models.ra import RA

class Test_RA():
    
    def test_create_instance_model(self):
        ra = RA(ano='19',numero='02009',digito='0')
        assert ra.ano == '19'
        assert ra.digito == '0'
        assert ra.numero == "02009"
        
    def test_ra_string(self):
        ra = RA(ano='19', numero='02009', digito='0')
        assert ra.toString() == "19.02009-0"
        
    def test_validator_error_numero(self):
        with pytest.raises(ValidationError) as error_info:
            ra = RA(ano='19',numero="020090",digito='0')
            
    def test_validator_error_ano(self):
        with pytest.raises(ValidationError) as error_info:
            ra = RA(ano='190',numero="02009",digito='0')
            
    def test_validator_error_digito(self):
        with pytest.raises(ValidationError) as error_info:
            ra = RA(ano='19',numero="02009",digito='00')