import pytest
from pydantic import ValidationError

from devmaua.src.enum.cargo import Cargo
from devmaua.src.enum.setor import Setor
from devmaua.src.enum.campus import Campus
from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco

from devmaua.src.models.administrativo import Administrativo
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco

class Test_Administrativo():
    
    def test_create_instance_model(self):
        email = Email(email='teste@teste.com',
                      tipo=TipoEmail.Privado,
                      prioridade = 1)
        end = Endereco(logradouro='rua de tal',
                       numero = 20,
                       cep='00000-000',
                       tipo = TipoEndereco.Residencial)
        tel = Telefone(tipo = TipoTelefone.Privado,
                       numero = '99999-9999',
                       ddd=11,
                       prioridade = 3)
        contato = Contato(emails = [email],
                          telefones = [tel],
                          enderecos = [end])
        
        adm = Administrativo(nome='jorge do teste',
                             contato = contato,
                             nascimento='1999-02-23',
                             ID='ABC01',
                             cargo=Cargo.Contador,
                             setor=Setor.Financeiro,
                             campus=Campus.SCS)
        
        assert adm._campus() == 'São Caetano Do Sul'
        assert adm._setor() == 'Financeiro'
        assert adm._cargo() == 'Contador'
        
    def test_validator_error_IDEmpty(self):
        with pytest.raises(ValidationError) as error_info:
            email = Email(email='teste@teste.com',
                        tipo=TipoEmail.Privado,
                        prioridade = 1)
            end = Endereco(logradouro='rua de tal',
                        numero = 20,
                        cep='00000-000',
                        tipo = TipoEndereco.Residencial)
            tel = Telefone(tipo = TipoTelefone.Privado,
                        numero = '99999-9999',
                        ddd=11,
                        prioridade = 3)
            contato = Contato(emails = [email],
                            telefones = [tel],
                            enderecos = [end])
            
            adm = Administrativo(nome='jorge do teste',
                                contato = contato,
                                nascimento='1999-02-23',
                                ID=' ',
                                cargo=Cargo.Contador,
                                setor=Setor.Financeiro,
                                campus=Campus.SCS)