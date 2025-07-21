
from django.urls import path
from .views import (
    portada_con_template,
    crear_cliente, 
    crear_producto,
    crear_mueble,
    buscar_cliente,
    buscar_producto,
    buscar_mueble,
    SofaCreateView,
    SillaListView,
    MesaComedorUpdateView
)

urlpatterns = [
    path('', portada_con_template, name='portada'),
    path('crear-cliente/<str:nombre>/', crear_cliente, name='crear-cliente'),
    path('crear-producto/<str:nombre>/', crear_producto, name='crear-producto'),
    path('crear-mueble/<str:nombre>/', crear_mueble, name='crear-mueble'),
    path('cliente/buscar/', buscar_cliente, name='buscar-cliente'),
    path('producto/buscar/', buscar_producto, name='buscar-producto'),
    path('mueble/buscar/', buscar_mueble, name='buscar-mueble'),
    path('sofa/nuevo/', SofaCreateView.as_view(), name='crear-sofa'),
    path('sillas/', SillaListView.as_view(), name='listar-sillas'),
    path('mesa/<int:pk>/editar/', MesaComedorUpdateView.as_view(), name='editar-mesa'),
]


