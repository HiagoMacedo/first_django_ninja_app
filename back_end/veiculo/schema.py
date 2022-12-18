from ninja import ModelSchema, Schema

from .models import Veiculo


class VeiculoSchema(ModelSchema):
    class Config:
        model = Veiculo
        model_fields = ['id',
                        'placa',
                        'modelo',
                        'numportas',
                        'arcondicionado',
                        'vencimentoseguro',
                        'codfilial',
                        'marca',
                        'ano',
                        'valordiaria']


class NotFound(Schema):
    message: str = "Veículo Not Found"
