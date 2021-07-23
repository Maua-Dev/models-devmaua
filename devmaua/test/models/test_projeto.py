import datetime
import pytest
from pydantic import ValidationError

from devmaua.src.enum.areas import Areas
from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.codigo_disciplina import CodigoDisciplina
from devmaua.src.enum.tronco import Tronco
from devmaua.src.enum.nome_curso import NomeCurso
from devmaua.src.enum.periodo import Periodo

from devmaua.src.models.professor import Professor
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.aluno import Aluno
from devmaua.src.models.ra import RA
from devmaua.src.models.projeto import Projeto

class Test_Projeto():
    
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
        
        ra = RA(ano='19',
                numero='02009',
                digito='0')               
        aluno = Aluno(nome='jorge do teste',
                          contato = contato,
                          nascimento='1999-02-23',
                          ra = ra,
                          curso = NomeCurso.EngenhariaDaComputacao,
                          serie = 3,
                          disciplinas=[CodigoDisciplina.ECM251],
                          periodo=Periodo.Diurno,
                          listaDPs=[],
                          hasDP=False)
        
        projeto = Projeto(nome='CubeSat',
                          area=Areas.NSEE,
                          cargaHorariaSemanal='20:00',
                          professorOrientador='0002',
                          participantes=[aluno, professor],
                          inicioDoPrograma='2021-02-20',
                          terminoDoPrograma='2021-10-20',
                          descricao='desc simples',
                          encontros=['2021-07-13 18:00:00', '2021-07-20 18:00:00'])
        
        assert projeto.nome == 'CubeSat'
        assert projeto._area() == 'Nucleo De Sistemas Eletrônicos Embarcados'
        assert projeto.cargaHorariaSemanal.hour == 20
        assert projeto.cargaHorariaSemanal.minute == 0
        assert projeto.professorOrientador == '0002'
        assert projeto.getAlunos() == [aluno]
        assert projeto.getProfessores() == [professor]
        assert projeto.participantes == [aluno, professor]
        assert projeto.inicioDoPrograma.day == 20
        assert projeto.inicioDoPrograma.month == 2
        assert projeto.inicioDoPrograma.year == 2021
        assert projeto.terminoDoPrograma.day == 20
        assert projeto.terminoDoPrograma.month == 10
        assert projeto.terminoDoPrograma.year == 2021
        assert projeto.descricao == 'desc simples'
        assert datetime.datetime(2021, 7, 20, 18, 0, 0) in projeto.encontros
        assert datetime.datetime(2021, 7, 13, 18, 0, 0) in projeto.encontros
        
    def test_validator_error_nomeIsEmpty(self):
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
                            disciplinas=[CodigoDisciplina.ECM251])
            ra = RA(ano='19',
                    numero='02009',
                    digito='0')               
            aluno = Aluno(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            ra = ra,
                            curso = NomeCurso.EngenhariaDaComputacao,
                            serie = 3,
                            disciplinas=[CodigoDisciplina.ECM251],
                            periodo=Periodo.Diurno,
                            listaDPs=[],
                            hasDP=False)
            
            projeto = Projeto(nome=' ',
                            area=Areas.NSEE,
                            cargaHorariaSemanal='20:00',
                            professorOrientador='0002',
                            participantes=[aluno, professor],
                            inicioDoPrograma='2021-02-20',
                            terminoDoPrograma='2021-10-20',
                            descricao='desc simples',
                            encontros=['2021-07-13 18:00:00', '2021-07-20 18:00:00'])
    
    def test_validator_error_nomeIsEmpty(self):
        with pytest.raises(ValidationError) as error_info:
                    
            projeto = Projeto(nome='CubeSat',
                            area=Areas.NSEE,
                            cargaHorariaSemanal='20:00',
                            professorOrientador='0002',
                            participantes=[],
                            inicioDoPrograma='2021-02-20',
                            terminoDoPrograma='2021-10-20',
                            descricao='desc simples',
                            encontros=['2021-07-13 18:00:00', '2021-07-20 18:00:00'])
            
    def test_validator_error_orientadorNotInParticipantes(self):
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
                            disciplinas=[CodigoDisciplina.ECM251])
            ra = RA(ano='19',
                    numero='02009',
                    digito='0')               
            aluno = Aluno(nome='jorge do teste',
                            contato = contato,
                            nascimento='1999-02-23',
                            ra = ra,
                            curso = NomeCurso.EngenhariaDaComputacao,
                            serie = 3,
                            disciplinas=[CodigoDisciplina.ECM251],
                            periodo=Periodo.Diurno,
                            listaDPs=[],
                            hasDP=False)
            
            projeto = Projeto(nome='CubeSat',
                            area=Areas.NSEE,
                            cargaHorariaSemanal='20:00',
                            professorOrientador='0003',
                            participantes=[aluno, professor],
                            inicioDoPrograma='2021-02-20',
                            terminoDoPrograma='2021-10-20',
                            descricao='desc simples',
                            encontros=['2021-07-13 18:00:00', '2021-07-20 18:00:00'])