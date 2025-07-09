from django.urls import path
from .views import (
    portada_con_template,
    crear_producto,
    crear_cliente,
    crear_categoria,
)

urlpatterns = [
    path('portada-con-template/', portada_con_template),
    path('crear-producto/', crear_producto),
    path('crear-cliente/', crear_cliente),
    path('crear-categoria/', crear_categoria),
]