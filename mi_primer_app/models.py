
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Mueble(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    tamano = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    





class Sofa(models.Model):
    tamano            = models.CharField(max_length=50)
    color             = models.CharField(max_length=50)
    tapizado          = models.CharField(max_length=100)
    fecha_produccion  = models.DateField()

class Silla(models.Model):
    tipo              = models.CharField(max_length=50)  
    color             = models.CharField(max_length=50)
    apoya_brazos      = models.BooleanField()
    fecha_fabricacion = models.DateField()

class Mesa(models.Model):
    forma             = models.CharField(max_length=50)   
    cantidad_patas    = models.IntegerField()
    color             = models.CharField(max_length=50)
    fecha             = models.DateField()



