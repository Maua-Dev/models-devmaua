import abc
from datetime import date, datetime
from pydantic import BaseModel, validator, ValidationError
from typing import Optional

from devmaua.src.enum.roles import Roles
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.telefone import Telefone


class Usuario(BaseModel):
    nome: str
    contato: Contato
    nascimento: date
    roles: list[Roles]
    timestamp: Optional[datetime]

    @validator('nome')
    def nome_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Nome is empty')
        return v.title()
    
    @validator('roles', check_fields=False)
    def roles_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('roles is empty')
        return v
    
    @validator('nascimento')
    # Assume-se que nenhum usuario da faculdade tem menos de 15 anos
    def year_is_valid(cls, v):
        if v.year > (datetime.now().year - 15):
            raise ValueError('ano invalido')
        return v

    @staticmethod
    def criarUsuarioPorDict(d: dict):
        """
        Instancia um usuário a partir de um dicionário com todos os atributos necessários
        :param d: dicinário do tipo:
        {
           "nome": "jorge do teste",
           "contato":{
              "telefones":[
                 {
                    "tipo":2,
                    "numero":"99999-9999",
                    "ddd":11,
                    "prioridade":3
                 }
              ],
              "emails":[
                 {
                    "email":"teste@teste.com",
                    "tipo":1,
                    "prioridade":1
                 }
              ],
              "enderecos":[
                 {
                    "logradouro":"rua de tal",
                    "numero":20,
                    "cep":"00000-000",
                    "complemento":null,
                    "tipo":1
                 }
              ]
           },
           "nascimento":"1999-02-23",
           "roles":[
              9
           ]
        }
        :return: intancia de Usuario com todos os atributos passados
        """

        try:
            emails = []
            enderecos = []
            telefones = []
            
            for email in d['contato']['emails']:
                emails.append(Email.criarEmailPorDict(email))
            
            for endereco in d['contato']['enderecos']:
                enderecos.append(Endereco.criarEnderecoPorDict(endereco))
                
            for telefone in d['contato']['telefones']:
                telefones.append(Telefone.criarTelefonePorDict(telefone))
                
            contato = Contato(emails = emails,
                              telefones = telefones,
                              enderecos = enderecos)

            usuario = Usuario(nome=d['nome'],
                              contato=contato,
                              nascimento=d['nascimento'],
                              roles=d['roles'])
            return usuario

        except ValidationError:
            raise ErroDadosUsuarioInvalidos

        except KeyError:
            raise ErroDadosUsuarioInvalidos
        
        except TypeError:
            raise ErroDadosUsuarioInvalidos


