from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Cliente, Producto, Mueble
from .forms import ClienteForm, ProductoForm, MuebleForm



def portada_con_template(request):
    return render(request, 'mi_primer_app/portada.html') 


# CREAR CLIENTE
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente.objects.create(**form.cleaned_data)
            return redirect('buscar-cliente')
    else:
        form = ClienteForm()
    return render(request, 'mi_primer_app/form_cliente.html', {'form': form})

# CREAR PRODUCTO
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            Producto.objects.create(**form.cleaned_data)
            return redirect('buscar-producto')
    else:
        form = ProductoForm()
    return render(request, 'mi_primer_app/form_producto.html', {'form': form})

# CREAR MUEBLE
def crear_mueble(request):
    if request.method == 'POST':
        form = MuebleForm(request.POST)
        if form.is_valid():
            Mueble.objects.create(**form.cleaned_data)
            return redirect('buscar-mueble')
    else:
        form = MuebleForm()
    return render(request, 'mi_primer_app/form_mueble.html', {'form': form})

# BUSCAR CLIENTE
def buscar_cliente(request):
    nombre = request.GET.get('nombre', '')
    resultados = Cliente.objects.filter(nombre__icontains=nombre)
    return render(request, 'mi_primer_app/buscar_cliente.html', {
        'nombre': nombre,
        'resultados': resultados
    })

# BUSCAR PRODUCTO
def buscar_producto(request):
    nombre = request.GET.get('nombre', '')
    resultados = Producto.objects.filter(nombre__icontains=nombre)
    return render(request, 'mi_primer_app/buscar_producto.html', {
        'nombre': nombre,
        'resultados': resultados
    })

# BUSCAR MUEBLE
def buscar_mueble(request):
    nombre = request.GET.get('nombre', '')
    resultados = Mueble.objects.filter(nombre__icontains=nombre)
    return render(request, 'mi_primer_app/buscar_mueble.html', {
        'nombre': nombre,
        'resultados': resultados
    })