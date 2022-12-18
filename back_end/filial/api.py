from ninja import Router
from typing import List, Optional

from .models import Filial
from .schema import FilialSchema, NotFound


router = Router(tags=["filial"])


@router.get("/", response={200: List[FilialSchema]})
def filiais(request,
            cidade: Optional[str] = None):
    if cidade:
        return Filial.objects.filter(cidade__icontains=cidade)
    return Filial.objects.all()


@router.post("/", response={201: FilialSchema})
def create_filial(request, data: FilialSchema):
    new_filial = Filial.objects.create(**data.dict())
    return 201, new_filial



@router.get("/{filial_id}", response={200: FilialSchema, 404: NotFound})
def filial(request, filial_id: int):
    try:
        filial = Filial.objects.get(codigo=filial_id)
        return 200, filial
    except Filial.DoesNotExist:
        return 404, NotFound


@router.put("/{filial_id}", response={200: FilialSchema, 404: NotFound})
def update_filial(request, filial_id: int, data: FilialSchema):
    try:
        filial = Filial.objects.get(codigo=filial_id)
        for key, value in data.dict().items():
            setattr(filial, key, value)
        filial.save()
        return 200, filial
    except Filial.DoesNotExist:
        return 404, NotFound


@router.delete("/{filial_id}", response={200: None, 404: NotFound})
def delete_filial(request, filial_id: int):
    try:
        filial = Filial.objects.get(codigo=filial_id)
        filial.delete()
        return 200
    except Filial.DoesNotExist:
        return 404, NotFound