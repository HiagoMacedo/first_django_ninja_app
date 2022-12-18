from ninja import Router
from typing import List, Optional

from cidade.models import Cidade
from cidade.schema import CidadeSchema, Error


router = Router(tags=["cidades"])


@router.get('/', response={200: List[CidadeSchema]})
def cidades(request, 
            nome: Optional[str] = None):
    if nome:
        return Cidade.objects.filter(nome__icontains=nome)
    return Cidade.objects.all()


@router.post('/', response={201: CidadeSchema})
def create_cidade(request, data: CidadeSchema):
    new_cidade = Cidade.objects.create(**data.dict())
    return 201, new_cidade



@router.get('/{cidade_id}', response={200: CidadeSchema, 404: Error})
def cidade(request, cidade_id: int):
    try:
        cidade = Cidade.objects.get(codigo=cidade_id)
        return 200, cidade
    
    except Cidade.DoesNotExist:
        return 404, {"message": "Cidade not found"}


@router.put('/{cidade_id}', response={200: CidadeSchema, 404: Error})
def update_cidade(request, cidade_id: int, data: CidadeSchema):
    try:
        cidade = Cidade.objects.get(codigo=cidade_id)
        for key, value in data.dict().items():
            setattr(cidade, key, value)
        cidade.save()
        return 200, cidade
    
    except Cidade.DoesNotExist:
        return 404, {"message": "Cidade not found"}


@router.delete('/{cidade_id}', response={200: None, 404: Error})
def delete_cidade(request, cidade_id: int):
    try:
        cidade = Cidade.objects.get(codigo=cidade_id)
        cidade.delete()
        return 200
    except Cidade.DoesNotExist:
        return 404, {"message": "Cidade not found"}