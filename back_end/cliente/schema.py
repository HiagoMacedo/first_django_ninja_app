from ninja import ModelSchema, Schema
from typing import Optional

from cliente.models import Cliente


class ClienteSchema(ModelSchema):
    class Config:
        model = Cliente
        model_fields = ['codigo', 'nome', 'rua', 'bairro', 'cidade', 'cep', 'uf', 'cpf', 'cnpj']


class Error(Schema):
    message: str = "Error"

    


    
# class CreateUpdateClienteSchema(Schema):
#     nome: str = "Nome"
#     rua: str = "Rua"
#     bairro: str = "Bairro"
#     cidade: str = "Cidade"
#     cep: str = "CEP"
#     uf: str = "UF"
#     cpf: str = None
#     cnpj: str = None