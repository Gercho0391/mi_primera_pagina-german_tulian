
from django.urls import path
from .views import (
    portada_con_template,
    crear_cliente, 
    crear_producto,
    crear_mueble,
    buscar_cliente,
    buscar_producto,
    buscar_mueble,
    SillaListView, 
    SillaCreateView, 
    SillaUpdateView, 
    SillaDeleteView,
    MesaListView,
    MesaCreateView, 
    MesaUpdateView, 
    MesaDeleteView,
    SofaListView, 
    SofaCreateView, 
    SofaUpdateView, 
    SofaDeleteView,
    MesaDetailView, 
    SofaDetailView, 
    SillaDetailView,
)

urlpatterns = [
    path('', portada_con_template, name='portada'),
    path('crear-cliente/<str:nombre>/', crear_cliente, name='crear-cliente'),
    path('crear-producto/<str:nombre>/', crear_producto, name='crear-producto'),
    path('crear-mueble/<str:nombre>/', crear_mueble, name='crear-mueble'),
    path('cliente/buscar/', buscar_cliente, name='buscar-cliente'),
    path('producto/buscar/', buscar_producto, name='buscar-producto'),
    path('mueble/buscar/', buscar_mueble, name='buscar-mueble'),
    path('sillas/', SillaListView.as_view(), name='silla-lista'),
    path('sillas/nueva/', SillaCreateView.as_view(), name='silla-crear'),
    path('sillas/<int:pk>/editar/', SillaUpdateView.as_view(), name='silla-actualizar'),
    path('sillas/<int:pk>/borrar/', SillaDeleteView.as_view(), name='silla-borrar'),
    path('sillas/<int:pk>/',  SillaDetailView.as_view(), name='silla-detalle'),
    path('mesas/', MesaListView.as_view(), name='mesa-lista'),
    path('mesas/nueva/', MesaCreateView.as_view(), name='mesa-crear'),
    path('mesas/<int:pk>/editar/', MesaUpdateView.as_view(), name='mesa-actualizar'),
    path('mesas/<int:pk>/borrar/', MesaDeleteView.as_view(), name='mesa-borrar'),
    path('mesas/<int:pk>/',   MesaDetailView.as_view(), name='mesa-detalle'),
    path('sofas/', SofaListView.as_view(), name='sofa-lista'),
    path('sofas/nueva/', SofaCreateView.as_view(), name='sofa-crear'),
    path('sofas/<int:pk>/editar/', SofaUpdateView.as_view(), name='sofa-actualizar'),
    path('sofas/<int:pk>/borrar/', SofaDeleteView.as_view(), name='sofa-borrar'),
    path('sofas/<int:pk>/',   SofaDetailView.as_view(), name='sofa-detalle'),
    
]


