from ninja import Schema, ModelSchema

from cidade.models import Cidade



class CidadeSchema(ModelSchema):
    class Config:
        model = Cidade
        model_fields = ['codigo',
                        'nome',
                        'populacao',
                        'anofundacao',
                        'uf']


class Error(Schema):
    message: str = "Error"