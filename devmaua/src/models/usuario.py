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
            email = Email(email=d['contato']['emails'][0]['email'],
                          tipo=d['contato']['emails'][0]['tipo'],
                          prioridade=d['contato']['emails'][0]['prioridade'])

            end = Endereco(logradouro=d['contato']['enderecos'][0]['logradouro'],
                           numero=d['contato']['enderecos'][0]['numero'],
                           cep=d['contato']['enderecos'][0]['cep'],
                           tipo=d['contato']['enderecos'][0]['tipo'],
                           complemento=d['contato']['enderecos'][0]['complemento'])
            tel = Telefone(tipo=d['contato']['telefones'][0]['tipo'],
                           numero=d['contato']['telefones'][0]['numero'],
                           ddd=d['contato']['telefones'][0]['ddd'],
                           prioridade=d['contato']['telefones'][0]['prioridade'])
            contato = Contato(emails=[email],
                              telefones=[tel],
                              enderecos=[end])

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


