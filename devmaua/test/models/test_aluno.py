import pytest
from pydantic import ValidationError

from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.roles import Roles
from devmaua.src.enum.nome_curso import NomeCurso
from devmaua.src.enum.periodo import Periodo
from devmaua.src.enum.codigo_disciplina import CodigoDisciplina

from devmaua.src.models.aluno import Aluno
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.ra import RA

class Test_Aluno():
    
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
        ra = RA(ano='19',
                numero='02009',
                digito='0')
        
        
        aluno = Aluno(nome='jorge do teste',
                          contato = contato,
                          nascimento='1999-02-23',
                          ra = ra,
                          curso = NomeCurso.ENGENHARIA_DA_COMPUTACAO,
                          serie = 3,
                          disciplinas=[CodigoDisciplina.ECM251],
                          periodo=Periodo.DIURNO,
                          listaDPs=[],
                          hasDP=False)
        
        assert aluno.roles == [Roles.ALUNO]
        assert aluno.ra.ano == '19'
        assert aluno.ra.numero == '02009'
        assert aluno.ra.digito == '0'
        assert aluno.curso == NomeCurso.ENGENHARIA_DA_COMPUTACAO
        assert aluno.serie == 3
        assert aluno.disciplinas == [CodigoDisciplina.ECM251]
        assert aluno.periodo == Periodo.DIURNO
        assert aluno.listaDPs == []
        assert aluno.hasDP == False
        
    def test_validator_error_RA(self):
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
            ra = RA(ano='190',
                    numero='02009',
                    digito='0')
            
            
            aluno = Aluno(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            ra = ra,
                            curso = NomeCurso.ENGENHARIA_DA_COMPUTACAO,
                            serie = 3,
                            disciplinas=[CodigoDisciplina.ECM251],
                            periodo=Periodo.DIURNO,
                            listaDPs=[],
                            hasDP=False)
            
    def test_validator_error_serie(self):
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
            ra = RA(ano='19',
                    numero='02009',
                    digito='0')
            
            
            aluno = Aluno(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            ra = ra,
                            curso = NomeCurso.ENGENHARIA_DA_COMPUTACAO,
                            serie = 6,
                            disciplinas=[CodigoDisciplina.ECM251],
                            periodo=Periodo.DIURNO,
                            listaDPs=[],
                            hasDP=False)
            
    def test_validator_error_hasDP(self):
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
            ra = RA(ano='19',
                    numero='02009',
                    digito='0')
            
            
            aluno = Aluno(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            ra = ra,
                            curso = NomeCurso.ENGENHARIA_DA_COMPUTACAO,
                            serie = 3,
                            disciplinas=[CodigoDisciplina.ECM251],
                            periodo=Periodo.DIURNO,
                            listaDPs=[],
                            hasDP=True)
            
    def test_validator_error_listaDPs(self):
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
            ra = RA(ano='19',
                    numero='02009',
                    digito='0')
            
            
            aluno = Aluno(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            ra = ra,
                            curso = NomeCurso.ENGENHARIA_DA_COMPUTACAO,
                            serie = 3,
                            disciplinas=[CodigoDisciplina.ECM251],
                            periodo=Periodo.DIURNO,
                            listaDPs=[CodigoDisciplina.ECM251],
                            hasDP=False)