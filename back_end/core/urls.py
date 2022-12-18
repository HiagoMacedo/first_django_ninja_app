from django.contrib import admin
from django.urls import path, include

from .api import api
# from cliente.api import api_cliente


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    # path('api/cliente/', api_cliente.urls),
]
