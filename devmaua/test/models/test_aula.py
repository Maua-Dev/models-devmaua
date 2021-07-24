from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.codigo_disciplina import CodigoDisciplina
from devmaua.src.enum.tronco import Tronco
from devmaua.src.enum.nome_curso import NomeCurso
from devmaua.src.enum.tipo_sala import TipoSala
from devmaua.src.enum.campus import Campus

from devmaua.src.models.aula import Aula
from devmaua.src.models.sala import Sala
from devmaua.src.models.professor import Professor
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco

class Test_Aula():
    
    
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
        professor = Professor(nome='jorge do teste',
                          contato = contato,
                          nascimento='1999-02-23',
                          ID='0002',
                          troncos=[Tronco.ELETRICA],
                          cursos=[NomeCurso.ENGENHARIA_DA_COMPUTACAO],
                          disciplinas=[CodigoDisciplina.ECM251])
        sala = Sala(bloco='U',
                    numeroDaSala=22,
                    tipo=[TipoSala.LABORATORIO],
                    campus = Campus.SCS)
        
        aula = Aula(disciplina=CodigoDisciplina.ECM251,
                    local=sala,
                    horario='2021-07-12 07:40:00',
                    duracao='01:40:00',
                    professor=professor)
        
        assert aula.termino() == '2021-07-12 09:20:00' 