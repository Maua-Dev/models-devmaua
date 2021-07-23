from devmaua.src.enum.grupos import Grupo
from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.nome_curso import NomeCurso
from devmaua.src.enum.periodo import Periodo
from devmaua.src.enum.codigo_disciplina import CodigoDisciplina
from devmaua.src.enum.cargo_representante import CargoRepresentante

from devmaua.src.models.aluno_representante import AlunoRepresentante
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.ra import RA

class Test_AlunoRepresentante():
    
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
        
        
        alunoRepresentante = AlunoRepresentante(nome='jorge do teste',
                          contato = contato,
                          nascimento='1999-02-23',
                          ra = ra,
                          curso = NomeCurso.EngenhariaDaComputacao,
                          serie = 3,
                          disciplinas=[CodigoDisciplina.ECM251],
                          periodo=Periodo.Diurno,
                          listaDPs=[],
                          hasDP=False,
                          cargo = CargoRepresentante.Titular,
                          grupoResponsavel = Grupo.G1)
        
        assert alunoRepresentante.cargo == CargoRepresentante.Titular
        assert alunoRepresentante.grupoResponsavel == Grupo.G1