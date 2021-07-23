import pytest
from pydantic import ValidationError

from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco

from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco


class Test_Contato():
    
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
        
        assert contato.emails[0].email == 'teste@teste.com'
        assert contato.emails[0].tipo == TipoEmail.Privado
        assert contato.emails[0].prioridade == 1
        
        assert contato.telefones[0].tipo == TipoTelefone.Privado
        assert contato.telefones[0].numero == '99999-9999'
        assert contato.telefones[0].ddd == 11
        assert contato.telefones[0]. prioridade == 3
        
        assert contato.enderecos[0].logradouro == 'rua de tal'
        assert contato.enderecos[0].numero == 20
        assert contato.enderecos[0].cep == '00000-000'
        assert contato.enderecos[0].tipo == TipoEndereco.Residencial
    
    def test_validator_error_email(self):
        with pytest.raises(ValidationError) as error_info:
            end = Endereco(logradouro='rua de tal',
                        numero = 20,
                        cep='00000-000',
                        tipo = TipoEndereco.Residencial)
            tel = Telefone(tipo = TipoTelefone.Privado,
                        numero = '99999-9999',
                        ddd=11,
                        prioridade = 3)
            contato = Contato(emails = [],
                            telefones = [tel],
                            enderecos = [end])
    
    def test_validator_error_endereco(self):
        with pytest.raises(ValidationError) as error_info:
            email = Email(email='teste@teste.com',
                        tipo=TipoEmail.Privado,
                        prioridade = 1)
            tel = Telefone(tipo = TipoTelefone.Privado,
                        numero = '99999-9999',
                        ddd=11,
                        prioridade = 3)
            contato = Contato(emails = [email],
                            telefones = [tel],
                            enderecos = [])
        
    def test_validator_error_telefone(self):
        with pytest.raises(ValidationError) as error_info:
            email = Email(email='teste@teste.com',
                        tipo=TipoEmail.Privado,
                        prioridade = 1)
            end = Endereco(logradouro='rua de tal',
                        numero = 20,
                        cep='00000-000',
                        tipo = TipoEndereco.Residencial)
            contato = Contato(emails = [email],
                            telefones = [],
                            enderecos = [end])