from ninja import Router
from typing import List, Optional

from .models import Veiculo
from .schema import VeiculoSchema, NotFound


router = Router(tags=['veiculos'])


@router.get('/', response={200: List[VeiculoSchema]})
def veiculos(request,
             placa: Optional[str] = None,
             modelo: Optional[str] = None):
    if placa:
        return Veiculo.objects.filter(placa__icontains=placa)
    if modelo:
        return Veiculo.objects.filter(modelo__icontains=modelo)

    return Veiculo.objects.all()


@router.post('/', response={201: VeiculoSchema})
def create_veiculo(request, data: VeiculoSchema):
    new_veiculo = Veiculo.objects.create(**data.dict())
    return 201, new_veiculo



@router.get('/{veiculo_id}', response={200: VeiculoSchema, 404: NotFound})
def veiculo(request, veiculo_id):
    try:
        veiculo = Veiculo.objects.get(id=veiculo_id)
        return 200, veiculo
    except Veiculo.DoesNotExist:
        return 404, NotFound


@router.put('/{veiculo_id}', response={200: VeiculoSchema, 404: NotFound})
def update_veiculo(request, veiculo_id, data: VeiculoSchema):
    try:
        veiculo = Veiculo.objects.get(id=veiculo_id)
        for attribute, value in data.dict().items():
            setattr(veiculo, attribute, value)
        veiculo.save()
        return 200, veiculo
    except Veiculo.DoesNotExist:
        return 404, NotFound


@router.delete('/{veiculo_id}', response={200: None, 404: NotFound})
def delete_veiculo(request, veiculo_id):
    try:
        veiculo = Veiculo.objects.get(id=veiculo_id)
        veiculo.delete()
        return 200
    except Veiculo.DoesNotExist:
        return 404, NotFound