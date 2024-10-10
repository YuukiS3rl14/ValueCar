from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class Comuna(models.Model):
    region = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Supermercado(models.Model):
    nombre = models.CharField(max_length=20)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    supermercado = models.ForeignKey(Supermercado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField(validators=[MaxValueValidator(999999)]) 
    descripcion = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    origen = models.CharField(max_length=200)
    fecha_actualizacion = models.DateField()

    def __str__(self):
        return self.nombre 
    
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre 
    
class Usuario(models.Model):
    tipousuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=256)

    def __str__(self):
        return self.nombre 

class Comentario(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=50)
    calificacion = models.IntegerField(validators=[MaxValueValidator(999999)]) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo



