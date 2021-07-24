import pytest
from pydantic import ValidationError
from datetime import datetime

from devmaua.src.enum.tipo_atividade import TipoAtividade
from devmaua.src.enum.status_avaliacao import StatusAvaliacao
from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.nome_curso import NomeCurso
from devmaua.src.enum.periodo import Periodo
from devmaua.src.enum.codigo_disciplina import CodigoDisciplina

from devmaua.src.models.atividade import Atividade
from devmaua.src.models.aluno import Aluno
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.ra import RA

class Test_Atividade():
    
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
        
        atividade = Atividade(tipo=TipoAtividade.PROVA,
                              prazo='2021-07-15 20:00',
                              alunos=[aluno],
                              tentativasPermitidas=3)
        
        
    def test_instance_methods(self):
        
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
        
        atividade = Atividade(tipo=TipoAtividade.PROVA,
                              prazo='2042-07-15 20:00',
                              alunos=[aluno],
                              tentativasPermitidas=3)
        
        atividade.set_nota(8)
        assert atividade.nota == 8.0
        assert atividade.nota_decimal() == 0.8
        assert atividade._status() == 'Não enviado'
        
        atividade._entrega()
        assert atividade.status == StatusAvaliacao.ENVIADO
        assert atividade.numeroDeEnvios == 1
        #assert atividade.dataEnvio == datetime.now() # Máquina do github da erro pelo tempo de isntanciar e verificar
        
    
    def test_validator_error_dataEntrega(self):
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
                            hasDP=False)
            
            atividade = Atividade(tipo=TipoAtividade.PROVA,
                                prazo='2021-07-15 20:00',
                                alunos=[aluno],
                                tentativasPermitidas=3,
                                dataEnvio = '2022-01-01 00:00')
            
            
    def test_validator_error_numeroDeTentativas(self):
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
                            hasDP=False)
            
            atividade = Atividade(tipo=TipoAtividade.PROVA,
                                prazo='2021-07-15 20:00',
                                alunos=[aluno],
                                tentativasPermitidas=3,
                                numeroDeEnvios = 4)
