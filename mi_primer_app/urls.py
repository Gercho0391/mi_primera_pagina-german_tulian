from django.urls import path
from .views import portada_con_template

urlpatterns = [
    path('portada-con-template/', portada_con_template),
]