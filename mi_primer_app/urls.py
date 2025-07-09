from django.urls import path
from .views import (
    portada_con_template,
    crear_producto_con_nombre,
    crear_cliente_con_nombre,
    crear_categoria_con_nombre,
)


urlpatterns = [
    path('portada-con-template/', portada_con_template),
    path('crear-producto/<str:nombre>/', crear_producto_con_nombre),
    path('crear-cliente/<str:nombre>/', crear_cliente_con_nombre),
    path('crear-categoria/<str:nombre>/', crear_categoria_con_nombre),
]