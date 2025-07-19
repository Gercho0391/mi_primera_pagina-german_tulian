from django.shortcuts import render
from .models import Cliente, Producto, Mueble


def portada_con_template(request):
    return render(request, 'mi_primer_app/portada.html') 


def crear_cliente(request, nombre=None):
    if nombre:
        Cliente.objects.create(nombre=nombre, apellido='ApellidoEjemplo', email='cliente@example.com')
    return render(request, 'mi_primer_app/crear_cliente.html', {'nombre': nombre})

def crear_producto(request, nombre=None):
    if nombre:
        Producto.objects.create(nombre=nombre, descripcion='Producto de ejemplo', precio=1000)
    return render(request, 'mi_primer_app/crear_producto.html', {'nombre': nombre})


def crear_mueble(request, nombre=None):
    if nombre:
        Mueble.objects.create(nombre=nombre, color='Blanco', tamano='Mediano')
    return render(request, 'mi_primer_app/crear_mueble.html', {'nombre': nombre})

def buscar_cliente(request):
    nombre   = request.GET.get('nombre', '')
    resultados = Cliente.objects.filter(nombre__icontains=nombre)
    return render(request, 'mi_primer_app/buscar_cliente.html', {'nombre': nombre, 'resultados': resultados})


def buscar_producto(request):
    nombre   = request.GET.get('nombre', '')
    resultados = Producto.objects.filter(nombre__icontains=nombre)
    return render(request, 'mi_primer_app/buscar_producto.html', {'nombre': nombre,'resultados': resultados })

def buscar_mueble(request):
    nombre   = request.GET.get('nombre', '')
    resultados = Mueble.objects.filter(nombre__icontains=nombre)
    return render(request, 'mi_primer_app/buscar_mueble.html', {'nombre': nombre, 'resultados': resultados})