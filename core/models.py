from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Automotora(models.Model):
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class TipoTransmicion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    automotora = models.ForeignKey(Automotora, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)  
    año = models.IntegerField()  
    precio = models.IntegerField()  
    descripcion = models.CharField(max_length=300) 
    imagen = models.ImageField(upload_to='autos/')  
    origen = models.URLField()  
    fecha_actualizacion = models.DateField(auto_now=True)
    kilometraje = models.IntegerField(null=True, blank=True)
    tipo_combustible = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
    potencia = models.CharField(max_length=50) 
    tipo_transmicion = models.ForeignKey(TipoTransmicion, on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    nuevo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre 
    
class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 

class Comentario(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=50)
    calificacion = models.IntegerField() 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'auto') 



