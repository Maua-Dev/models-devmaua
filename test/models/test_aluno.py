import pytest
from pydantic import ValidationError

from src.enum.tipo_email import TipoEmail
from src.enum.tipo_telefone import TipoTelefone
from src.enum.tipo_endereco import TipoEndereco
from src.enum.roles import Roles
from src.enum.nome_curso import NomeCurso
from src.enum.periodo import Periodo
from src.enum.codigo_disciplina import CodigoDisciplina

from src.models.aluno import Aluno
from src.models.contato import Contato
from src.models.email import Email
from src.models.telefone import Telefone
from src.models.endereco import Endereco
from src.models.ra import RA

class Test_Aluno():
    
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
        ra = RA(ano='19',
                numero='02009',
                digito='0')
        
        
        aluno = Aluno(nome='jorge do teste',
                          contato = contato,
                          nascimento='1999-02-23',
                          roles=[Roles.Aluno],
                          ra = ra,
                          curso = NomeCurso.EngenhariaDaComputacao,
                          serie = 3,
                          disciplinas=[CodigoDisciplina.ECM251],
                          periodo=Periodo.Diurno,
                          listaDPs=[],
                          hasDP=False)
        
        assert aluno.ra.ano == '19'
        assert aluno.ra.numero == '02009'
        assert aluno.ra.digito == '0'
        assert aluno.curso == NomeCurso.EngenhariaDaComputacao
        assert aluno.serie == 3
        assert aluno.disciplinas == [CodigoDisciplina.ECM251]
        assert aluno.periodo == Periodo.Diurno
        assert aluno.listaDPs == []
        assert aluno.hasDP == False
        
    def test_validator_error_RA(self):
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
            ra = RA(ano='190',
                    numero='02009',
                    digito='0')
            
            
            aluno = Aluno(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            roles=[Roles.Aluno],
                            ra = ra,
                            curso = NomeCurso.EngenhariaDaComputacao,
                            serie = 3,
                            disciplinas=[CodigoDisciplina.ECM251],
                            periodo=Periodo.Diurno,
                            listaDPs=[],
                            hasDP=False)
            
    def test_validator_error_serie(self):
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
            ra = RA(ano='19',
                    numero='02009',
                    digito='0')
            
            
            aluno = Aluno(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            roles=[Roles.Aluno],
                            ra = ra,
                            curso = NomeCurso.EngenhariaDaComputacao,
                            serie = 6,
                            disciplinas=[CodigoDisciplina.ECM251],
                            periodo=Periodo.Diurno,
                            listaDPs=[],
                            hasDP=False)
            
    def test_validator_error_hasDP(self):
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
            ra = RA(ano='19',
                    numero='02009',
                    digito='0')
            
            
            aluno = Aluno(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            roles=[Roles.Aluno],
                            ra = ra,
                            curso = NomeCurso.EngenhariaDaComputacao,
                            serie = 3,
                            disciplinas=[CodigoDisciplina.ECM251],
                            periodo=Periodo.Diurno,
                            listaDPs=[],
                            hasDP=True)
            
    def test_validator_error_listaDPs(self):
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
            ra = RA(ano='19',
                    numero='02009',
                    digito='0')
            
            
            aluno = Aluno(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            roles=[Roles.Aluno],
                            ra = ra,
                            curso = NomeCurso.EngenhariaDaComputacao,
                            serie = 3,
                            disciplinas=[CodigoDisciplina.ECM251],
                            periodo=Periodo.Diurno,
                            listaDPs=[CodigoDisciplina.ECM251],
                            hasDP=False)