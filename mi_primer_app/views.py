from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Cliente, Producto, Mueble, Sofa, Silla, Mesa
from .forms import ClienteForm, ProductoForm, MuebleForm, SofaForm, SillaForm, MesaForm

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


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




def about(request):
    return render(request, "mi_primer_app/about.html")




# Silla

class SillaListView(ListView):
    model = Silla
    template_name = 'mi_primer_app/silla_lista.html'
    context_object_name = 'sillas'

class SillaCreateView(CreateView):
    model = Silla
    form_class = SillaForm
    template_name = 'mi_primer_app/silla_crear.html'

    def get_success_url(self):
        return reverse_lazy('silla-lista') + '#silla-lista'

class SillaUpdateView(UpdateView):
    model = Silla
    form_class = SillaForm
    template_name = 'mi_primer_app/silla_actualizar.html'

    def get_success_url(self):
        return reverse_lazy('silla-lista') + '#silla-lista'

class SillaDeleteView(DeleteView):
    model = Silla
    template_name = 'mi_primer_app/silla_borrar.html'

    def get_success_url(self):
        return reverse_lazy('silla-lista') + '#silla-lista'

class SillaDetailView(DetailView):
    model = Silla
    template_name = 'mi_primer_app/silla_detalle.html'
    context_object_name = 'silla'


# Mesa

class MesaListView(ListView):
    model = Mesa
    template_name = 'mi_primer_app/mesa_lista.html'
    context_object_name = 'mesas'

class MesaCreateView(CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mi_primer_app/mesa_crear.html'

    def get_success_url(self):
        return reverse_lazy('mesa-lista') + '#mesa-lista'

class MesaUpdateView(UpdateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mi_primer_app/mesa_actualizar.html'

    def get_success_url(self):
        return reverse_lazy('mesa-lista') + '#mesa-lista'

class MesaDeleteView(DeleteView):
    model = Mesa
    template_name = 'mi_primer_app/mesa_borrar.html'

    def get_success_url(self):
        return reverse_lazy('mesa-lista') + '#mesa-lista'

class MesaDetailView(DetailView):
    model = Mesa
    template_name = 'mi_primer_app/mesa_detalle.html'
    context_object_name = 'mesa'


# Sofa

class SofaListView(ListView):
    model = Sofa
    template_name = 'mi_primer_app/sofa_lista.html'
    context_object_name = 'sofas'

class SofaCreateView(CreateView):
    model = Sofa
    form_class = SofaForm
    template_name = 'mi_primer_app/sofa_crear.html'

    def get_success_url(self):
        return reverse_lazy('sofa-lista') + '#sofa-lista'

class SofaUpdateView(UpdateView):
    model = Sofa
    form_class = SofaForm
    template_name = 'mi_primer_app/sofa_actualizar.html'

    def get_success_url(self):
        return reverse_lazy('sofa-lista') + '#sofa-lista'

class SofaDeleteView(DeleteView):
    model = Sofa
    template_name = 'mi_primer_app/sofa_borrar.html'

    def get_success_url(self):
        return reverse_lazy('sofa-lista') + '#sofa-lista'

class SofaDetailView(DetailView):
    model = Sofa
    template_name = 'mi_primer_app/sofa_detalle.html'
    context_object_name = 'sofa'