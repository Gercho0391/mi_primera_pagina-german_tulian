from django.shortcuts import render
from .models import Categoria, Producto, Cliente


def portada_con_template(request):
    return render(request, 'mi_primer_app/portada.html') 

def crear_categoria(request):
    nueva_categoria = Categoria(
        nombre="sillon",
        descripcion="sillon de dos y tres cuerpos"
    )
    nueva_categoria.save()
    return render(request, "mi_primer_app/crear_categoria.html", {"categoria": nueva_categoria})


def crear_producto(request):
    nuevo_producto = Producto(
        nombre="Mesa de madera",
        descripcion="Mesa con respaldo de madera maciza",
        precio=15000
    )
    nuevo_producto.save()
    return render(request, "mi_primer_app/crear_producto.html", {"producto": nuevo_producto})


def crear_cliente(request):
    nuevo_cliente = Cliente(
        nombre="German",
        apellido="Tulian",
        email="German@example.com"
    )
    nuevo_cliente.save()
    return render(request, "mi_primer_app/crear_cliente.html", {"cliente": nuevo_cliente})


