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

def buscar_cliente(request):
    if request.method == "GET":
        nombre = request.GET.get("nombre", '')
        Cliente.objects.filter(nombre__icontains=nombre)
        return render(request, "mi_primer_app/buscar_cliente.html", {"cliente": nombre, "nombre": nombre})


def buscar_producto(request):
    if request.method == "GET":
        nombre = request.GET.get("nombre", '')
        Producto.objects.filter(nombre__icontains=nombre)
        return render(request, "mi_primer_app/buscar_producto.html", {"busqueda": nombre, "nombre": nombre})

def cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'mi_primer_app/clientes.html', {'clientes': clientes})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'mi_primer_app/productos.html', {'productos': productos})

def muebles(request):
    muebles = Producto.objects.filter(nombre__icontains="mueble")
    return render(request, 'mi_primer_app/muebles.html', {'muebles': muebles})



