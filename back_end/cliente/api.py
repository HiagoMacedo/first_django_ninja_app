from ninja import Router
from typing import List, Optional

from cliente.models import Cliente
from cliente.schema import (ClienteSchema,
                            Error)

router = Router(tags=["clientes"])



@router.get('/', response= List[ClienteSchema])
def clientes(request, 
             nome: Optional[str] = None, 
             uf: Optional[str] = None):
    if nome and uf:
        return Cliente.objects.filter(nome__icontains=nome, uf__icontains=uf)
    if nome:
        return Cliente.objects.filter(nome__icontains=nome)
    if uf:
        return Cliente.objects.filter(uf__icontains=uf)
    
    return Cliente.objects.all()


@router.post('/', response={201: ClienteSchema})
def create_cliente(request, data: ClienteSchema):
    cliente = Cliente.objects.create(**data.dict())
    return 201, cliente



@router.get('/{cliente_id}', response={200: ClienteSchema, 404: Error})
def cliente(request, cliente_id: int):
    try:
        cliente = Cliente.objects.get(codigo=cliente_id)
        return 200, cliente
    
    except Cliente.DoesNotExist:
        return 404, {"message": "Cliente not found."}


@router.put('/{cliente_id}', response={200: ClienteSchema, 404: Error})
def put_cliente(request, cliente_id: int, data: ClienteSchema):
    try:
        cliente = Cliente.objects.get(codigo=cliente_id)
        for attribute, value in data.dict().items():
            setattr(cliente, attribute, value)
        cliente.save()
        return 200, cliente
    
    except Cliente.DoesNotExist:
        return 404, {"message": "Cliente not found."}


# @router.patch('/{cliente_id}', response={200: ClienteSchema, 404: Error})
# def patch_cliente(request, cliente_id: int, data: ClienteSchema):
#     try:
#         cliente = Cliente.objects.get(codigo=cliente_id)
#         for attribute, value in data.dict().items():
#             setattr(cliente, attribute, value)
#         cliente.save()
#         return 200, cliente
    
#     except Cliente.DoesNotExist:
#         return 404, {"message": "Cliente not found."}


@router.delete('/{cliente_id}', response={200: ClienteSchema, 404: Error})
def delete_cliente(request, cliente_id: int):
    try:
        cliente = Cliente.objects.get(codigo=cliente_id)
        cliente.delete()
        return 200
    
    except Cliente.DoesNotExist:
        return 404, {"message": "Cliente not found."}