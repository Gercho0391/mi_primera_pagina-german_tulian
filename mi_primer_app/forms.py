from django import forms
from .models import Cliente, Producto, Categoria, Mueble, Sofa, Silla, Mesa



class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre",      max_length=100)
    apellido = forms.CharField(label="Apellido",    max_length=100)
    email = forms.EmailField(label="Email")
    fecha_registro    = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))


class CategoriaForm(forms.Form):
    nombre = forms.CharField(
        label="Categoría",
        max_length=50,
        help_text="Ej: Sillones, Mesas, Sillas…"
    )


class ProductoForm(forms.ModelForm):
    class Meta:
        model  = Producto
        fields = ['nombre', 'precio', 'categoria']
        widgets = {'categoria': forms.Select(attrs={'class': 'form-control'}),}


class MuebleForm(forms.ModelForm):
    class Meta:
        model  = Mueble
        fields = ['nombre', 'color', 'tamano']
        labels = {'tamano': 'Tamaño',}
        widgets = {'color': forms.TextInput(attrs={'placeholder': 'Ej: Gris, Marrón…'}),'tamano': forms.TextInput(attrs={'placeholder': 'Ej: 2 cuerpos'}),}




class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['forma', 'cantidad_patas', 'color', 'fecha']
        labels = {
          'forma': 'Forma de la mesa',
          'cantidad_patas': 'Número de patas',
          'color': 'Color',
          'fecha': 'Fecha'
        }
        widgets = {'fecha': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),}

class SillaForm(forms.ModelForm):
    class Meta:
        model = Silla
        fields = ['tipo', 'color', 'apoya_brazos', 'fecha']
        labels = {
            'tipo': 'Tipo de silla',
            'color': 'Color',
            'apoya_brazos': '¿Con apoyabrazos?',
            'fecha': 'Fecha '
        }
        widgets = {'fecha': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),}
    
class SofaForm(forms.ModelForm):
    class Meta:
        model = Sofa
        fields = ['tamano', 'color', 'tapizado', 'fecha']
        labels = {
            'tamano': 'Tamaño del sofá',
            'color': 'Color',
            'tapizado': 'Tapizado',
            'fecha': 'Fecha'
        }
        widgets = {'fecha': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),}