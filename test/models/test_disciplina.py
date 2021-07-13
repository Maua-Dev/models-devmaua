from src.enum.tipo_email import TipoEmail
from src.enum.tipo_telefone import TipoTelefone
from src.enum.tipo_endereco import TipoEndereco
from src.enum.roles import Roles
from src.enum.codigo_disciplina import CodigoDisciplina
from src.enum.tronco import Tronco
from src.enum.nome_curso import NomeCurso
from src.enum.tipo_sala import TipoSala
from src.enum.campus import Campus
from src.enum.semestralidade import Semestralidade
from src.enum.tipo_disciplina import TipoDisciplina
from src.enum.periodo import Periodo

from src.models.aula import Aula
from src.models.sala import Sala
from src.models.professor import Professor
from src.models.contato import Contato
from src.models.email import Email
from src.models.telefone import Telefone
from src.models.endereco import Endereco
from src.models.aluno import Aluno
from src.models.ra import RA
from src.models.disciplina import Disciplina

class Test_Disciplina():
    
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
        
        sala = Sala(bloco='U',
                    numeroDaSala=22,
                    tipo=[TipoSala.Laboratorio],
                    campus = Campus.SCS)
        
        aula = Aula(disciplina=CodigoDisciplina.ECM251,
                    local=sala,
                    horario='2021-07-12 07:40:00',
                    duracao='01:40:00',
                    professor=professor)
        
        disciplina = Disciplina(codigo=CodigoDisciplina.ECM251,
                                tipo=TipoDisciplina.Graduacao,
                                semestralidade=Semestralidade.A,
                                profOrientador=professor,
                                professores=[professor],
                                alunosMatriculados=[aluno],
                                aulas=[aula],
                                ofereceDp=True)
        
        assert disciplina.nome() == 'Linguagens de Programação I'
        assert disciplina.codigo == CodigoDisciplina.ECM251
        assert disciplina.tipo == TipoDisciplina.Graduacao
        assert disciplina.semestralidade == Semestralidade.A
        assert disciplina.profOrientador == professor
        assert disciplina.professores == [professor]
        assert disciplina.alunosMatriculados == [aluno]
        assert disciplina.aulas == [aula]
        assert disciplina.ofereceDp == True
        