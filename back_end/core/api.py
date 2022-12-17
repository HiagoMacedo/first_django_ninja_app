from ninja import NinjaAPI, Schema

api = NinjaAPI()


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