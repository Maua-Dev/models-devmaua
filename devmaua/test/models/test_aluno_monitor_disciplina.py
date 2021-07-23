from datetime import datetime

from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.nome_curso import NomeCurso
from devmaua.src.enum.codigo_disciplina import CodigoDisciplina
from devmaua.src.enum.tipo_sala import TipoSala
from devmaua.src.enum.campus import Campus
from devmaua.src.enum.semestralidade import Semestralidade
from devmaua.src.enum.tipo_disciplina import TipoDisciplina
from devmaua.src.enum.periodo import Periodo
from devmaua.src.enum.tronco import Tronco

from devmaua.src.models.aluno_monitor_diciplina import AlunoMonitorDisciplina
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.ra import RA
from devmaua.src.models.sala import Sala
from devmaua.src.models.professor import Professor
from devmaua.src.models.aula import Aula
from devmaua.src.models.monitoria import Monitoria
from devmaua.src.models.disciplina import Disciplina
from devmaua.src.models.curso import Curso
from devmaua.src.models.aluno import Aluno

class Test_AlunoMonitorDisciplina():
    
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
        sala = Sala(bloco='U',
                    numeroDaSala=22,
                    tipo=[TipoSala.Laboratorio],
                    campus = Campus.SCS)
        aula = Aula(disciplina=CodigoDisciplina.ECM251,
                    local=sala,
                    horario='2021-07-12 07:40:00',
                    duracao='01:40:00',
                    professor=professor)
        
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
        disciplina = Disciplina(codigo=CodigoDisciplina.ECM251,
                                tipo=TipoDisciplina.Graduacao,
                                semestralidade=Semestralidade.A,
                                profOrientador=professor,
                                professores=[professor],
                                alunosMatriculados=[aluno],
                                aulas=[aula],
                                ofereceDp=True)
        curso = Curso(tronco=Tronco.Eletrica,
                      disciplinas=[disciplina],
                      periodo=Periodo.Diurno,
                      nome=NomeCurso.EngenhariaDaComputacao,
                      duracao=5)
        
        monitoria = Monitoria(disciplina=disciplina,
                              curso=curso,
                              cargaHorariaSemanal='04:00',
                              professorOrientador='0002',
                              monitor=ra,
                              inicioDoPrograma='2021-02-20',
                              terminoDoPrograma='2021-10-20',
                              descricao='desc simples',
                              atendimentos=['2021-07-13 18:00:00', '2021-07-20 18:00:00'])
        
        alunoMonitor = AlunoMonitorDisciplina(nome='jorge do teste',
                          contato = contato,
                          nascimento='1999-02-23',
                          ra = ra,
                          curso = NomeCurso.EngenhariaDaComputacao,
                          serie = 3,
                          disciplinas=[CodigoDisciplina.ECM251],
                          periodo=Periodo.Diurno,
                          listaDPs=[],
                          hasDP=False,
                          monitoria = monitoria)
        
        assert alunoMonitor.monitoria.disciplina == disciplina
        assert alunoMonitor.monitoria.curso == curso
        assert alunoMonitor.monitoria.cargaHorariaSemanal.hour == 4
        assert alunoMonitor.monitoria.professorOrientador == '0002'
        assert alunoMonitor.monitoria.monitor.numero == '02009'
        assert alunoMonitor.monitoria.inicioDoPrograma.day == 20
        assert alunoMonitor.monitoria.descricao == 'desc simples'
        assert datetime(2021, 7, 20, 18, 0) in alunoMonitor.monitoria.atendimentos
        assert datetime(2021, 7, 13, 18, 0) in alunoMonitor.monitoria.atendimentos