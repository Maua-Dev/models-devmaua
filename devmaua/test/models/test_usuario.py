import pytest
from pydantic import ValidationError

from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.roles import Roles

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco

class Test_Usuario():
    
    def test_create_instance_model(self):
        
        email = Email(email='teste@teste.com',
                      tipo=TipoEmail.PRIVADO,
                      prioridade = 1)
        end = Endereco(logradouro='rua de tal',
                       numero = 20,
                       cep='00000-000',
                       tipo = TipoEndereco.RESIDENCIAL)
        tel = Telefone(tipo = TipoTelefone.PRIVADO,
                       numero = '99999-9999',
                       ddd=11,
                       prioridade = 3)
        contato = Contato(emails = [email],
                          telefones = [tel],
                          enderecos = [end])
        
        
        usuario = Usuario(nome='jorge do teste',
                          contato = contato,
                          nascimento='1999-02-23',
                          roles=[Roles.ALUNO])
        
        assert usuario.nome == 'Jorge Do Teste'
        
        assert usuario.contato.emails[0].email == 'teste@teste.com'
        assert usuario.contato.emails[0].tipo == TipoEmail.PRIVADO
        assert usuario.contato.emails[0].prioridade == 1
        
        assert usuario.contato.telefones[0].tipo == TipoTelefone.PRIVADO
        assert usuario.contato.telefones[0].numero == '99999-9999'
        assert usuario.contato.telefones[0].ddd == 11
        assert usuario.contato.telefones[0]. prioridade == 3
        
        assert usuario.contato.enderecos[0].logradouro == 'rua de tal'
        assert usuario.contato.enderecos[0].numero == 20
        assert usuario.contato.enderecos[0].cep == '00000-000'
        assert usuario.contato.enderecos[0].tipo == TipoEndereco.RESIDENCIAL
        
        assert usuario.nascimento.year == 1999
        assert usuario.nascimento.month == 2
        assert usuario.nascimento.day == 23
        
        assert usuario.roles == [Roles.ALUNO]
        
    def test_validator_error_nome(self):
        with pytest.raises(ValidationError) as error_info:
            email = Email(email='teste@teste.com',
                        tipo=TipoEmail.PRIVADO,
                        prioridade = 1)
            
            end = Endereco(logradouro='rua de tal',
                        numero = 20,
                        cep='00000-000',
                        tipo = TipoEndereco.RESIDENCIAL)
            
            tel = Telefone(tipo = TipoTelefone.PRIVADO,
                        numero = '99999-9999',
                        ddd=11,
                        prioridade = 3)
            
            contato = Contato(emails = [email],
                            telefones = [tel],
                            enderecos = [end])            
            
            usuario = Usuario(nome='',
                            contato = contato,
                            nascimento='1999-02-23',
                            roles=[Roles.ALUNO])
    
    def test_validator_error_contato(self):
        with pytest.raises(ValidationError) as error_info:
            usuario = Usuario(nome='jorge do teste',
                              contato = None,
                              nascimento='1999-02-23',
                              roles=[Roles.ALUNO])
            
    def test_validator_error_nascimento(self):
        with pytest.raises(ValidationError) as error_info:
            email = Email(email='teste@teste.com',
                        tipo=TipoEmail.PRIVADO,
                        prioridade = 1)
            
            end = Endereco(logradouro='rua de tal',
                        numero = 20,
                        cep='00000-000',
                        tipo = TipoEndereco.RESIDENCIAL)
            
            tel = Telefone(tipo = TipoTelefone.PRIVADO,
                        numero = '99999-9999',
                        ddd=11,
                        prioridade = 3)
            
            contato = Contato(emails = [email],
                            telefones = [tel],
                            enderecos = [end])            
            
            usuario = Usuario(nome='jorge do teste',
                            contato = contato,
                            nascimento='2010-02-23',
                            roles=[Roles.ALUNO])
            
    def test_validator_error_roles(self):
        with pytest.raises(ValidationError) as error_info:
            email = Email(email='teste@teste.com',
                        tipo=TipoEmail.PRIVADO,
                        prioridade = 1)
            
            end = Endereco(logradouro='rua de tal',
                        numero = 20,
                        cep='00000-000',
                        tipo = TipoEndereco.RESIDENCIAL)
            
            tel = Telefone(tipo = TipoTelefone.PRIVADO,
                        numero = '99999-9999',
                        ddd=11,
                        prioridade = 3)
            
            contato = Contato(emails = [email],
                            telefones = [tel],
                            enderecos = [end])            
            
            usuario = Usuario(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            roles=[])

        def test_criar_usuario_por_dict(self):
            d = {
                "nome": "Jorge do Teste",
                "contato": {
                    "telefones": [
                        {
                            "tipo": 2,
                            "numero": "99999-9999",
                            "ddd": 11,
                            "prioridade": 3
                        }
                    ],
                    "emails": [
                        {
                            "email": "teste@teste.com",
                            "tipo": 1,
                            "prioridade": 1
                        }
                    ],
                    "enderecos": [
                        {
                            "logradouro": "rua de tal",
                            "numero": 20,
                            "cep": "00000-000",
                            "complemento": None,
                            "tipo": 1
                        }
                    ]
                },
                "nascimento": "1999-02-23",
                "roles": [
                    9
                ]
            }
            usuario = Usuario.criarUsuarioPorDict(d)
            assert usuario.nome == 'Jorge Do Teste'

            assert usuario.contato.emails[0].email == 'teste@teste.com'
            assert usuario.contato.emails[0].tipo == TipoEmail.PRIVADO
            assert usuario.contato.emails[0].prioridade == 1

            assert usuario.contato.telefones[0].tipo == TipoTelefone.PRIVADO
            assert usuario.contato.telefones[0].numero == '99999-9999'
            assert usuario.contato.telefones[0].ddd == 11
            assert usuario.contato.telefones[0].prioridade == 3

            assert usuario.contato.enderecos[0].logradouro == 'rua de tal'
            assert usuario.contato.enderecos[0].numero == 20
            assert usuario.contato.enderecos[0].cep == '00000-000'
            assert usuario.contato.enderecos[0].tipo == TipoEndereco.RESIDENCIAL

            assert usuario.nascimento.year == 1999
            assert usuario.nascimento.month == 2
            assert usuario.nascimento.day == 23

            assert usuario.roles == [Roles.ALUNO]


