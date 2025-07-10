from django.contrib import admin
from .models import Producto, Cliente, Categoria
# Register your models here.

modelos_admin = [Producto, Cliente, Categoria]

admin.site.register(modelos_admin)


