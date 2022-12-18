from ninja import Schema, ModelSchema

from .models import Filial


class FilialSchema(ModelSchema):
    class Config:
        model = Filial
        model_fields = ['codigo',
                        'telefone',
                        'rua',
                        'bairro',
                        'cidade',
                        'cep',
                        'idcidade',
                        'uf'
                        ]


class NotFound(Schema):
    message: str = "Filial not found"