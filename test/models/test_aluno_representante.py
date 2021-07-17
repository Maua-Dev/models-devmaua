from src.enum.grupos import Grupo
from src.enum.tipo_email import TipoEmail
from src.enum.tipo_telefone import TipoTelefone
from src.enum.tipo_endereco import TipoEndereco
from src.enum.roles import Roles
from src.enum.nome_curso import NomeCurso
from src.enum.periodo import Periodo
from src.enum.codigo_disciplina import CodigoDisciplina
from src.enum.cargo_representante import CargoRepresentante

from src.models.aluno_representante import AlunoRepresentante
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