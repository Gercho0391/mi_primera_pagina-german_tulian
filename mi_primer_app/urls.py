from django.urls import path
from .views import (
    portada_con_template,
    crear_producto,
    crear_cliente,
    crear_categoria,
    buscar_producto,
    buscar_cliente,
    buscar_mueble,
    )

urlpatterns = [
    path('portada-con-template/', portada_con_template),
    path('crear-producto/', crear_producto),
    path('crear-cliente/', crear_cliente),
    path('crear-categoria/', crear_categoria),
    path('cliente/buscar/', buscar_cliente, name='buscar-cliente'),
    path('producto/buscar/', buscar_producto, name='buscar-producto'),
    path('mueble/buscar/', buscar_mueble, name='buscar-mueble')
]