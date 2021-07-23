import pytest
from pydantic import ValidationError

from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.roles import Roles
from devmaua.src.enum.codigo_disciplina import CodigoDisciplina
from devmaua.src.enum.tronco import Tronco
from devmaua.src.enum.nome_curso import NomeCurso

from devmaua.src.models.professor import Professor
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco

class Test_Professor():
    
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
        
        
        professor = Professor(nome='jorge do teste',
                          contato = contato,
                          nascimento='1999-02-23',
                          ID='0002',
                          troncos=[Tronco.Eletrica],
                          cursos=[NomeCurso.EngenhariaDaComputacao],
                          disciplinas=[CodigoDisciplina.ECM251])
        
        assert professor.roles == [Roles.Professor]
        assert professor.ID == '0002'
        assert professor.troncos == [Tronco.Eletrica]
        assert professor.cursos == [NomeCurso.EngenhariaDaComputacao]
        assert professor.disciplinas == [CodigoDisciplina.ECM251]
        
    def test_validator_error_ID(self):
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
            
            
            professor = Professor(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            ID=None,
                            troncos=[Tronco.Eletrica],
                            cursos=[NomeCurso.EngenhariaDaComputacao],
                            disciplinas=[CodigoDisciplina.ECM251])
            
    def test_validator_error_troncos(self):
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
            
            
            professor = Professor(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            ID='0002',
                            troncos=[],
                            cursos=[NomeCurso.EngenhariaDaComputacao],
                            disciplinas=[CodigoDisciplina.ECM251])
            
    def test_validator_error_cursos(self):
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
            
            
            professor = Professor(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            ID='0002',
                            troncos=[Tronco.Eletrica],
                            cursos=[],
                            disciplinas=[CodigoDisciplina.ECM251])
            
    def test_validator_error_disciplinas(self):
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
            
            
            professor = Professor(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            ID='0002',
                            troncos=[Tronco.Eletrica],
                            cursos=[NomeCurso.EngenhariaDaComputacao],
                            disciplinas=[])