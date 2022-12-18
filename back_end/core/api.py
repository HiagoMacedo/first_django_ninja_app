from ninja import NinjaAPI, Schema
from cliente.api import router as cliente_router
from cidade.api import router as cidade_router
from filial.api import router as filial_router



api = NinjaAPI()

api.add_router('/clientes/', cliente_router)
api.add_router('/cidades/', cidade_router)
api.add_router('/filial/', filial_router)

class HelloSchema(Schema):
    name: str = "world"


@api.post('/hello')
def hello_world(request, data: HelloSchema):
    return f"Hello {data.name}"


@api.get('/math/{a}and{b}')
def math(request, a: int, b: int):
    return {"add": a + b,
            "multiply": a * b}


class UserSchema(Schema):
    username: str
    email: str
    first_name: str
    last_name: str

class Error(Schema):
    message: str


@api.get('/me', response={200: UserSchema, 403: Error})
def user(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Login first"}
    return request.user